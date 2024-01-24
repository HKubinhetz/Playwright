import time
import asyncio

from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep


async def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://comgas.service-now.com/comgas_itsm?id=sc_cat_item&sys_id=29f7a3bb1b027890fa2442ece54bcb5a")

    storage = context.storage_state(path="state.json")

    await browser.close()

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
