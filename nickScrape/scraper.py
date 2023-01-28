import nest_asyncio
nest_asyncio.apply()
from playwright.sync_api import sync_playwright


if __name__ == "__main__":
    pw = sync_playwright().start()
    chrome = pw.chromium.launch(headless=False)
    page = chrome.new_page()
    page.goto("https://twitch.tv")