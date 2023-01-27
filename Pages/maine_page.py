from .base_page import BasePage
from .locators import maine_page_locators

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.page.locator(maine_page_locators.login_link)
        login_link.click()
