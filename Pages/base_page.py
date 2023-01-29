from Pages.locators import Base_page_locators


class BasePage():

    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url, wait_until='domcontentloaded')

    def search(self, search):
        self.page.locator(Base_page_locators.field_find).fill(search)
        self.page.locator(Base_page_locators.button_find).click()


    def go_to_cart(self):
        self.page.locator(Base_page_locators.button_go_to_cart).click()


    def check_url(self, checked_url):
        print(self.page.url())
        assert self.page.url() == checked_url



