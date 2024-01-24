import time
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())

# TODO - Implement user authentication with all the time needed for finishing, then storages cookies.
# # Save storage state into the file.
# storage = await context.storage_state(path="state.json")
#
# # Create a new context with the saved storage state.
# context = await browser.new_context(storage_state="state.json")

