import pytest
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest_playwright
from playwright.sync_api import Playwright, sync_playwright, expect


class maine_page_locators():
    login_link = '[id="login_link"]'


class Login_page_locators():

    field_login_user_name = '//input[@name="login-username"]'
    field_login_password = '[name="login-password"]'
    field_registration_email = '[name="registration-email"]'
    field_registration_password1 = '[name="registration-password1"]'
    field_registration_password2 = '[name="registration-password2"]'
    button_login = '[name="login_submit"]'
    button_registration = '[name="registration_submit"]'


class Product_page_locators():

    button_add_product = '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'

class Base_page_locators():

    field_find = '[name="q"]'
    button_find = '//input[@value="Найти"]'
    button_go_to_cart = '//a[@class="btn btn-default"]'

class Searching_results_locators():

    button_add_to_cart = '//button[@data-loading-text="Добавление..."]'
    alert_about_add_product = '[class="alert alert-safe alert-noicon alert-success  fade in"]'






