import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('http://automationpractice.com/index.php')
    time.sleep(3)
    await page.click('a[title="Women"]');
    time.sleep(5)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())