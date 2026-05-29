from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            storage_state="state.json",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()

        print("Navigating to dashboard...")
        page.goto("https://basecamp.com/2325709/")
        page.wait_for_timeout(5000)  # wait 5 seconds for any dynamic content to load

        html = page.content()
        with open("dashboard.html", "w") as f:
            f.write(html)
        print("Saved dashboard.html")
        browser.close()


if __name__ == "__main__":
    main()
