import time

import pytest
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest_playwright


from playwright.sync_api import Playwright, sync_playwright, expect

# def test_page_open(page):
#
#     page.goto('https://demo.playwright.dev/todomvc/#/')
#     assert page.url == 'https://demo.playwright.dev/todomvc/#/'
#     print(page.url)
#     field = page.locator('[placeholder="What needs to be done?"]')
#     field.fill("Закончить курс по playwright")
#     field.press('Enter')
#     field.fill("Добавить в резюме, что умею автоматизировать")
#     field.press('Enter')
#     todo_item = page.locator('[data-testid="todo-item"]')
#     time.sleep(5)