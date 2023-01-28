from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://collegestation.craigslist.org/search/cta?hasPic=1&purveyor=owner&query=dodge#search=1~grid~0~0")
    print(page.content())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
