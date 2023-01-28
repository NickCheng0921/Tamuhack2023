from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    #time.sleep(1)
    page.goto("https://collegestation.craigslist.org/search/cta?hasPic=1&purveyor=owner#search=1~grid~0~0")
    time.sleep(1)
    #page.screenshot(path="image.png")

    soup = BeautifulSoup(page.content(), features="lxml")
    #print(soup.find("div", class_="cl-gallery"))
    parsed = []
    for item in soup.find_all("div", class_="cl-gallery"):
        #parsed.append({
        img = item.find("img", src=True)
        if img is not None:
            print(img["src"])

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
