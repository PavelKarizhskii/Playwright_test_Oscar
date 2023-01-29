from .base_page import BasePage
from .locators import Login_page_locators
import pytest
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest_playwright
from playwright.sync_api import Playwright, sync_playwright, expect


class Login_page(BasePage):

    def should_be_login_page(self):
        self.should_be_login_page_url()
        self.should_be_login_form()
        self.should_be_registration_form()

    def should_be_login_form(self):
        expect(self.page.locator(Login_page_locators.button_login)).to_be_visible()
        expect(self.page.locator(Login_page_locators.field_login_password)).to_be_visible()
        expect(self.page.locator(Login_page_locators.field_login_user_name)).to_be_visible()

    def should_be_registration_form(self):
        expect(self.page.locator(Login_page_locators.field_registration_email)).to_be_visible()
        expect(self.page.locator(Login_page_locators.button_registration)).to_be_visible()
        expect(self.page.locator(Login_page_locators.field_registration_password1)).to_be_visible()
        expect(self.page.locator(Login_page_locators.field_registration_password2)).to_be_visible()

    def should_be_login_page_url(self):
        print(f'curent url:{str(self.page.url)}')
        assert self.page.url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/' or self.page.url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', "некорректный url страницы логина"