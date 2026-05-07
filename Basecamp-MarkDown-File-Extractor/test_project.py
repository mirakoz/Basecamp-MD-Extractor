from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            storage_state="state.json",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        project_id = "19872116"
        base = f"https://basecamp.com/2325709/projects/{project_id}"
        
        print("Navigating to project home...")
        page.goto(base)
        page.wait_for_timeout(2000)
        with open("project.html", "w") as f:
            f.write(page.content())
            
        print("Navigating to messages...")
        page.goto(f"{base}/messages")
        page.wait_for_timeout(2000)
        with open("messages.html", "w") as f:
            f.write(page.content())

        print("Navigating to todos...")
        page.goto(f"{base}/todos")
        page.wait_for_timeout(2000)
        with open("todos.html", "w") as f:
            f.write(page.content())

        print("Saved debug html files.")
        browser.close()

if __name__ == "__main__":
    main()
