import os
import json
import yaml
import re
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import markdownify

STATE_FILE = "state.json"
BASECAMP_URL = "https://basecamp.com/2325709/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
EXPORTS_DIR = Path.home() / "Downloads" / "Basecamp-Exports"
MANIFEST_FILE = "sync_manifest_bc2.json"

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "r") as f:
            return json.load(f)
    return {}

def save_manifest(manifest):
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)

def is_synced(manifest, url):
    return url in manifest

def mark_synced(manifest, url):
    manifest[url] = datetime.now().isoformat()
    save_manifest(manifest)

def sanitize_filename(name):
    # Remove invalid characters for filenames and prevent path traversal
    name = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    # Strip leading/trailing dots and spaces to prevent hidden files/traversal
    name = name.strip(". ")
    return name if name else "unnamed"

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove Basecamp UI buttons, forms, and admin controls
    # Also explicitly remove scripts and metadata to prevent XSS and leakage
    selectors_to_remove = [
        'script', 'style', 'meta', 'link', 'form',
        '.action_button', '.button', '.admin', '.controls',
        '.button_to', '.edit', '.delete', '.trash', 'header menu'
    ]
    for selector in selectors_to_remove:
        for element in soup.select(selector):
            element.decompose()
            
    return str(soup)

def generate_markdown(title, content_html, url, author="Unknown", date="Unknown"):
    content_md = markdownify.markdownify(content_html, heading_style="ATX")
    
    frontmatter = {
        "title": title,
        "url": url,
        "author": author,
        "date": date,
        "type": "basecamp-export"
    }
    
    md_content = "---\n"
    md_content += yaml.dump(frontmatter, sort_keys=False)
    md_content += "---\n\n"
    md_content += f"# {title}\n\n"
    md_content += content_md
    return md_content

def scroll_to_bottom(page):
    print("    Scrolling to load all items...")
    last_height = page.evaluate("document.body.scrollHeight")
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(3000)  # Wait for page to load new content
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            # Try scrolling up slightly and back down
            page.evaluate("window.scrollTo(0, document.body.scrollHeight - 500)")
            page.wait_for_timeout(500)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(3000)
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
        last_height = new_height

def extract_projects(page):
    print(f"Navigating to dashboard: {BASECAMP_URL}")
    page.goto(BASECAMP_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body", timeout=10000)
    
    links = page.query_selector_all("a[href*='/projects/']")
    projects = []
    seen_urls = set()
    
    for link in links:
        url = link.get_attribute("href")
        if url and "/projects/" in url and "/messages" not in url and "/todos" not in url and "/todolists" not in url:
            full_url = f"https://basecamp.com{url}" if url.startswith("/") else url
            if full_url not in seen_urls:
                title = link.inner_text().strip()
                if title and len(title) > 0 and not title[0].isdigit(): 
                    # Clean the title of newlines like "Last updated..."
                    title = title.split('\n')[0].strip()
                    projects.append({"title": title, "url": full_url})
                    seen_urls.add(full_url)
    
    return projects

def extract_page_content(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body", timeout=10000)
    
    title = page.title().split(" - ")[0].strip() # Clean title
    html_content = ""
    
    # Try to extract the main content container. Basecamp 2 uses #content, .panel, or specific article classes.
    try:
        content_el = page.query_selector("article.message, article.todolist, #content, .panel")
        if content_el:
            html_content += content_el.inner_html()
            
        comments_el = page.query_selector(".comments, #comments")
        if comments_el:
            html_content += "\n<hr>\n<h2>Comments</h2>\n"
            html_content += comments_el.inner_html()
            
    except Exception as e:
        print(f"    Warning: Could not extract specific containers for {url}: {e}")
        html_content = page.content() # Fallback to entire page if selectors fail
        
    html_content = clean_html(html_content)
    return title, html_content

def scrape_project(page, project, manifest):
    project_title = sanitize_filename(project["title"])
    project_dir = EXPORTS_DIR / project_title
    project_dir.mkdir(exist_ok=True)
    
    messages_dir = project_dir / "Messages"
    messages_dir.mkdir(exist_ok=True)
    todos_dir = project_dir / "To-dos"
    todos_dir.mkdir(exist_ok=True)

    print(f"Scraping Project: {project['title']}")
    
    # --- Scrape Discussions (Messages, Topics, Files) ---
    print(f"  -> Discovering Discussions...")
    page.goto(project["url"] + "/topics", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body")
    scroll_to_bottom(page)
    
    # Grab all links inside the inbox table that represent discussions
    msg_urls = set()
    links = page.query_selector_all("table.inbox a")
    if not links:
        links = page.query_selector_all("article.topic a.subject")
        
    for link in links:
        href = link.get_attribute("href")
        if href and "/new" not in href and "/people/" not in href:
            full_url = f"https://basecamp.com{href}" if href.startswith("/") else href
            msg_urls.add(full_url)
            
    print(f"  -> Found {len(msg_urls)} discussions.")
    new_count = 0
    for i, m_url in enumerate(msg_urls):
        if is_synced(manifest, m_url):
            print(f"    -> Skipping (already synced): {m_url}")
            continue
        print(f"    -> Extracting discussion {i+1}/{len(msg_urls)}: {m_url}")
        try:
            title, html = extract_page_content(page, m_url)
            md = generate_markdown(title, html, m_url)
            filename = sanitize_filename(title) + ".md"
            with open(messages_dir / filename, "w") as f:
                f.write(md)
            mark_synced(manifest, m_url)
            new_count += 1
        except Exception as e:
            print(f"       Failed to extract discussion {m_url}: {e}")
    print(f"  -> Synced {new_count} new discussions (skipped {len(msg_urls) - new_count})")
            
    # --- Scrape To-dos ---
    print(f"  -> Discovering To-dos...")
    todo_urls = set()
    
    # 1. Active to-dos
    page.goto(project["url"] + "/todos", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body")
    scroll_to_bottom(page)
    for link in page.query_selector_all("a[href*='/todolists/']"):
        href = link.get_attribute("href")
        if href and "trash" not in href:
            href = href.split("#")[0]
            full_url = f"https://basecamp.com{href}" if href.startswith("/") else href
            todo_urls.add(full_url)
            
    # 2. Completed to-dos
    print(f"  -> Discovering Completed To-dos...")
    page.goto(project["url"] + "/todolists/completed", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2000)
    scroll_to_bottom(page)
    for link in page.query_selector_all("a[href*='/todolists/']"):
        href = link.get_attribute("href")
        if href and "trash" not in href and "/completed" not in href:
            href = href.split("#")[0]
            full_url = f"https://basecamp.com{href}" if href.startswith("/") else href
            todo_urls.add(full_url)
            
    print(f"  -> Found {len(todo_urls)} to-do lists.")
    new_count = 0
    for i, t_url in enumerate(todo_urls):
        if is_synced(manifest, t_url):
            print(f"    -> Skipping (already synced): {t_url}")
            continue
        print(f"    -> Extracting To-do list {i+1}/{len(todo_urls)}: {t_url}")
        try:
            title, html = extract_page_content(page, t_url)
            md = generate_markdown(title, html, t_url)
            filename = sanitize_filename(title) + ".md"
            with open(todos_dir / filename, "w") as f:
                f.write(md)
            mark_synced(manifest, t_url)
            new_count += 1
        except Exception as e:
            print(f"       Failed to extract to-do list {t_url}: {e}")
    print(f"  -> Synced {new_count} new to-do lists (skipped {len(todo_urls) - new_count})")

def main():
    if not os.path.exists(STATE_FILE):
        print(f"Error: {STATE_FILE} not found. Please run auth.py first to log in.")
        return
        
    EXPORTS_DIR.mkdir(exist_ok=True)
    manifest = load_manifest()
    print(f"Manifest loaded: {len(manifest)} URLs already synced.")
    
    print("Starting Playwright to extract data...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STATE_FILE, user_agent=USER_AGENT)
        page = context.new_page()
        
        projects = extract_projects(page)
        print(f"Found {len(projects)} projects.")
        
        for project in projects:
            scrape_project(page, project, manifest)
            
        browser.close()
        print("Extraction complete.")

if __name__ == "__main__":
    main()
