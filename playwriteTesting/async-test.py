import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("https://collegestation.craigslist.org/search/cta?hasPic=1&purveyor=owner&query=dodge#search=1~grid~0~0")
    # other actions...
    await page.screenshot(path="image.png")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
