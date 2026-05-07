import time
from playwright.sync_api import sync_playwright

STATE_FILE = "state_bc3.json"
BASECAMP_URL = "https://3.basecamp.com/6116304/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STATE_FILE, user_agent=USER_AGENT)
        page = context.new_page()
        
        print(f"Navigating to {BASECAMP_URL}")
        page.goto(BASECAMP_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000) # Wait for cards to render
        
        with open("bc3_dashboard.html", "w") as f:
            f.write(page.content())
            
        print("Dashboard HTML saved to bc3_dashboard.html")
        
        links = page.query_selector_all("a")
        buckets = set()
        for l in links:
            href = l.get_attribute("href")
            if href and ("/buckets/" in href or "/projects/" in href):
                print(f"Found link: {l.inner_text().strip()} -> {href}")
                buckets.add(href)
                
        browser.close()

if __name__ == "__main__":
    main()
