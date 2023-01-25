import pytest
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest_playwright
from playwright.sync_api import Playwright, sync_playwright, expect


from playwright.sync_api import Playwright, sync_playwright, expect


# @pytest.fixture(scope="function")
# def browsers():
#     print("\nstart browser for test..")
#     yield browsers
#     print("\nquit browser..")
#     browsers.quit()




@pytest.fixture(scope="function")
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()