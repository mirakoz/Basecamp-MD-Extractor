import time
from playwright.sync_api import sync_playwright

STATE_FILE = "state.json"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STATE_FILE, user_agent=USER_AGENT)
        page = context.new_page()
        
        # Arzum project discussions
        url = "https://basecamp.com/2325709/projects/19926871/topics"
        print(f"Navigating to {url}")
        page.goto(url)
        page.wait_for_selector("body")
        
        print("Scrolling...")
        last_height = page.evaluate("document.body.scrollHeight")
        loops = 0
        while loops < 10:
            # Scroll down by pressing PageDown multiple times to trigger scroll events
            page.keyboard.press("End")
            page.wait_for_timeout(2000)
            
            # Or use wheel
            page.mouse.wheel(0, 5000)
            page.wait_for_timeout(2000)
            
            new_height = page.evaluate("document.body.scrollHeight")
            print(f"Height: {last_height} -> {new_height}")
            if new_height == last_height:
                # try clicking 'Load more' if it exists, sometimes Basecamp uses a button
                load_more = page.query_selector("a.load_more, .infinite_scroll_link")
                if load_more and load_more.is_visible():
                    print("Found load more button, clicking...")
                    load_more.click()
                    page.wait_for_timeout(2000)
                    continue
                else:
                    break
            last_height = new_height
            loops += 1
            
        print("Done scrolling.")
        links = page.query_selector_all("article.topic a.subject")
        hrefs = set([l.get_attribute('href') for l in links])
        if not hrefs: # Fallback
            links = page.query_selector_all("table.inbox a")
            hrefs = set([l.get_attribute('href') for l in links if '/new' not in l.get_attribute('href')])
        
        print(f"Found {len(hrefs)} links.")
        for h in list(hrefs)[:10]:
            print(h)
        
        with open("arzum_topics.html", "w") as f:
            f.write(page.content())
            
        browser.close()

if __name__ == "__main__":
    main()
