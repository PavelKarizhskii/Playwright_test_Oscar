from .base_page import BasePage
from Pages.locators import Searching_results_locators

class Searching_results_page(BasePage):


    def add_product_by_number(self, number=0):

        self.page.locator(Searching_results_locators.button_add_to_cart).locator(f'nth={number}').click()

    def ckeck_add_Python_Learning(self):

        text = self.page.locator(Searching_results_locators.alert_about_add_product).locator(f'nth=0').text_content()
        assert 'Learning Python был добавлен в вашу корзину.' in text, "запись о добавлении книги Learning Python не найдена"

