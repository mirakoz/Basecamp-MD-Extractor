import os
from playwright.sync_api import sync_playwright

STATE_FILE = "state.json"
BASECAMP_URL = "https://basecamp.com/2325709/"

def main():
    print("Starting Playwright...")
    with sync_playwright() as p:
        # Launch browser visibly so you can log in
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        print(f"Navigating to {BASECAMP_URL}")
        page.goto(BASECAMP_URL)
        
        print("\n" + "="*50)
        print("Please log in to your Basecamp account in the browser window.")
        print("After you have successfully logged in and can see your dashboard,")
        input("Press ENTER in this terminal to save your session...")
        print("="*50 + "\n")
        
        # Save the authentication state (cookies, local storage)
        context.storage_state(path=STATE_FILE)
        
        print(f"Session saved to {STATE_FILE}. You can now run the extractor script.")
        browser.close()

if __name__ == "__main__":
    main()
