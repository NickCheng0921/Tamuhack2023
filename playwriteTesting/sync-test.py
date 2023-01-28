from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
time.sleep(1)
page.goto("https://collegestation.craigslist.org/search/cta?hasPic=1&purveyor=owner&query=dodge#search=1~grid~0~0")
time.sleep(1)
print(page.content())
browser.close()

playwright.stop()
