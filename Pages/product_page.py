from .base_page import BasePage
from Pages.locators import Product_page_locators
from Pages.locators import Product_page_locators

class Product_page(BasePage):

    def click_button_add_product(self):
        self.page.locator(Product_page_locators.button_add_product).click()