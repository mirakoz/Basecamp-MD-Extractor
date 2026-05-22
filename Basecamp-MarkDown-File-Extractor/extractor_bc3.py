import os
import json
import yaml
import re
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import markdownify

STATE_FILE = "state_bc3.json"
BASECAMP_URL = "https://3.basecamp.com/6116304/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
EXPORTS_DIR = Path.home() / "Downloads" / "Basecamp-Exports"
MANIFEST_FILE = "sync_manifest_bc3.json"

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
    # Remove invalid characters for filenames (including path separators)
    name = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    # Remove leading dots to prevent hidden files and path traversal
    name = name.lstrip('.')
    # Prevent path traversal by removing ".." and redundant dots
    name = re.sub(r'\.\.+', '.', name)
    if not name:
        name = "unnamed"
    return name

def clean_html_bc3(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove Basecamp 3 UI buttons, avatars, forms, and admin controls
    selectors_to_remove = [
        '.action-sheet', '.button', '.btn', '.avatar', 'form', 
        '.nav', '.menu', '.tooltip', '.header__menu', 
        '.record-tools', '.push-button', '.chat__tools'
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
        "type": "basecamp3-export"
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
        page.wait_for_timeout(3000)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight - 500)")
            page.wait_for_timeout(500)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(3000)
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
        last_height = new_height

def extract_page_content(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body", timeout=10000)
    
    title = page.title().split(" - ")[0].strip()
    html_content = ""
    
    try:
        # Basecamp 3 main content containers
        content_el = page.query_selector("main, .record, .chat, article")
        if content_el:
            html_content += content_el.inner_html()
            
        comments_el = page.query_selector(".comments")
        if comments_el:
            html_content += "\n<hr>\n<h2>Comments</h2>\n"
            html_content += comments_el.inner_html()
            
    except Exception as e:
        print(f"    Warning: Could not extract specific containers for {url}: {e}")
        html_content = page.content()
        
    html_content = clean_html_bc3(html_content)
    return title, html_content

def scrape_project(context, project, manifest):
    page = context.new_page()
    project_title = sanitize_filename(project["title"])
    project_dir = EXPORTS_DIR / project_title
    project_dir.mkdir(exist_ok=True, parents=True)

    print(f"Scraping Project: {project['title']}")
    
    # Identify the tools available in the project
    page.goto(project["url"], wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body")
    
    links = page.query_selector_all(".project__tool a, a.card__link, article a, a")
    tool_links = {"message_boards": None, "todosets": None, "vaults": None, "chats": None}
    
    for l in links:
        href = l.get_attribute("href")
        if not href: continue
        full_href = f"https://3.basecamp.com{href}" if href.startswith("/") else href
        if "/message_boards/" in href and not tool_links["message_boards"]: tool_links["message_boards"] = full_href
        if "/todosets/" in href and not tool_links["todosets"]: tool_links["todosets"] = full_href
        if "/vaults/" in href and not tool_links["vaults"]: tool_links["vaults"] = full_href
        if "/chats/" in href and not tool_links["chats"]: tool_links["chats"] = full_href
            
    # --- 1. Messages ---
    if tool_links["message_boards"]:
        messages_dir = project_dir / "Messages"
        messages_dir.mkdir(exist_ok=True)
        print(f"  -> Discovering Messages...")
        page.goto(tool_links['message_boards'], wait_until="domcontentloaded", timeout=60000)
        scroll_to_bottom(page)
        
        msg_urls = set()
        for l in page.query_selector_all("a[href*='/messages/']"):
            href = l.get_attribute("href")
            if href and "/new" not in href:
                full = f"https://3.basecamp.com{href}" if href.startswith("/") else href
                msg_urls.add(full)
                
        print(f"  -> Found {len(msg_urls)} messages.")
        new_count = 0
        for i, m_url in enumerate(msg_urls):
            if is_synced(manifest, m_url):
                print(f"    -> Skipping (already synced): {m_url}")
                continue
            print(f"    -> Extracting message {i+1}/{len(msg_urls)}")
            try:
                title, html = extract_page_content(page, m_url)
                md = generate_markdown(title, html, m_url)
                filename = sanitize_filename(title) + ".md"
                with open(messages_dir / filename, "w") as f:
                    f.write(md)
                mark_synced(manifest, m_url)
                new_count += 1
            except Exception as e:
                print(f"       Failed to extract {m_url}: {e}")
        print(f"  -> Synced {new_count} new messages (skipped {len(msg_urls) - new_count})")

    # --- 2. To-dos ---
    if tool_links["todosets"]:
        todos_dir = project_dir / "To-dos"
        todos_dir.mkdir(exist_ok=True)
        print(f"  -> Discovering To-dos...")
        page.goto(tool_links['todosets'], wait_until="domcontentloaded", timeout=60000)
        scroll_to_bottom(page)
        
        todo_urls = set()
        for l in page.query_selector_all("a[href*='/todolists/']"):
            href = l.get_attribute("href")
            if href and "trash" not in href and "/edit" not in href and "/new" not in href:
                href = href.split("#")[0]
                full = f"https://3.basecamp.com{href}" if href.startswith("/") else href
                todo_urls.add(full)
                
        print(f"  -> Found {len(todo_urls)} to-do items/lists.")
        new_count = 0
        for i, t_url in enumerate(todo_urls):
            if is_synced(manifest, t_url):
                print(f"    -> Skipping (already synced): {t_url}")
                continue
            print(f"    -> Extracting To-do {i+1}/{len(todo_urls)}")
            try:
                title, html = extract_page_content(page, t_url)
                md = generate_markdown(title, html, t_url)
                filename = sanitize_filename(title) + ".md"
                with open(todos_dir / filename, "w") as f:
                    f.write(md)
                mark_synced(manifest, t_url)
                new_count += 1
            except Exception as e:
                print(f"       Failed to extract {t_url}: {e}")
        print(f"  -> Synced {new_count} new to-dos (skipped {len(todo_urls) - new_count})")

    # --- 3. Docs ---
    if tool_links["vaults"]:
        docs_dir = project_dir / "Docs"
        docs_dir.mkdir(exist_ok=True)
        print(f"  -> Discovering Docs...")
        page.goto(tool_links['vaults'], wait_until="domcontentloaded", timeout=60000)
        scroll_to_bottom(page)
        
        doc_urls = set()
        for l in page.query_selector_all("a[href*='/documents/']"):
            href = l.get_attribute("href")
            if href and "/new" not in href:
                full = f"https://3.basecamp.com{href}" if href.startswith("/") else href
                doc_urls.add(full)
                
        print(f"  -> Found {len(doc_urls)} documents.")
        new_count = 0
        for i, d_url in enumerate(doc_urls):
            if is_synced(manifest, d_url):
                print(f"    -> Skipping (already synced): {d_url}")
                continue
            print(f"    -> Extracting doc {i+1}/{len(doc_urls)}")
            try:
                title, html = extract_page_content(page, d_url)
                md = generate_markdown(title, html, d_url)
                filename = sanitize_filename(title) + ".md"
                with open(docs_dir / filename, "w") as f:
                    f.write(md)
                mark_synced(manifest, d_url)
                new_count += 1
            except Exception as e:
                print(f"       Failed to extract {d_url}: {e}")
        print(f"  -> Synced {new_count} new docs (skipped {len(doc_urls) - new_count})")

    # --- 4. Campfire ---
    if tool_links["chats"]:
        chats_dir = project_dir / "Campfire"
        chats_dir.mkdir(exist_ok=True)
        print(f"  -> Extracting Campfire...")
        chat_url = tool_links['chats']
        try:
            # Basecamp chats require scrolling UP to load history.
            # We will just grab the visible chat for now or do a quick scroll up.
            page.goto(chat_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector("body")
            
            # Simple scroll up loop
            print("    Scrolling up to load chat history...")
            for _ in range(5): 
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(2000)
                
            title, html = extract_page_content(page, chat_url)
            md = generate_markdown(title, html, chat_url)
            filename = "Campfire_Chat.md"
            with open(chats_dir / filename, "w") as f:
                f.write(md)
        except Exception as e:
            print(f"       Failed to extract Campfire: {e}")
            
    page.close()


def extract_projects(page):
    print(f"Navigating to dashboard: {BASECAMP_URL}")
    page.goto(BASECAMP_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("body", timeout=10000)
    
    projects = []
    seen_urls = set()
    
    articles = page.query_selector_all("article.card--project")
    for article in articles:
        title = article.get_attribute("data-sortable-name")
        link = article.query_selector("a")
        
        if title and link:
            href = link.get_attribute("href")
            if href and ("/projects/" in href or "/buckets/" in href) and href not in seen_urls:
                full_url = f"https://3.basecamp.com{href}" if href.startswith("/") else href
                projects.append({"title": title.strip(), "url": full_url})
                seen_urls.add(href)
    
    return projects

def main():
    if not os.path.exists(STATE_FILE):
        print(f"Error: {STATE_FILE} not found. Please run auth_bc3.py first to log in.")
        return
        
    print("Starting Playwright to extract Basecamp 3 data...")
    manifest = load_manifest()
    print(f"Manifest loaded: {len(manifest)} URLs already synced.")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = browser.new_context(storage_state=STATE_FILE, user_agent=USER_AGENT)
        page = context.new_page()
        
        projects = extract_projects(page)
        page.close()
        
        # Deduplicate by title
        unique_projects = {}
        for p in projects:
            if p["title"] not in unique_projects:
                unique_projects[p["title"]] = p
        projects = list(unique_projects.values())
        
        print(f"Found {len(projects)} projects/teams.")
        
        for project in projects:
            scrape_project(context, project, manifest)
            
        browser.close()
        print("Extraction complete.")

if __name__ == "__main__":
    main()
