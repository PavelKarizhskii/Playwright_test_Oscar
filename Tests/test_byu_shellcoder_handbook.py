import time

import pytest
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest_playwright

from Pages.base_page import BasePage
from Pages.locators import Product_page_locators
from Pages.product_page import Product_page
from Pages.maine_page import MainPage
from Pages.searching_results_page import Searching_results_page


from playwright.sync_api import Playwright, sync_playwright, expect


def test_byu_shellcoder_handbook(page):

    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(page, link)
    main_page.open()
    time.sleep(10)
    main_page.search("Python")
    searh_page = Searching_results_page(page, page.url)
    searh_page.add_product_by_number()
    searh_page.ckeck_add_Python_Learning()

