import time
from Pages.maine_page import MainPage
from Pages.login_page import Login_page



#
def test_guest_can_go_to_login_pag(page):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(page, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = Login_page(page, page.url)
    login_page.should_be_login_page()



#
# def go_to_login_page(page):
#     login_link = page.locator('[id="login_link"]')
#     login_link.click()
