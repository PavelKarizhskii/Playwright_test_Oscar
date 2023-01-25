import time


def test_guest_can_go_to_login_page(page):
    link = "http://selenium1py.pythonanywhere.com/"
    page.goto(link)
    login_link = page.locator('[id="login_link"]')
    login_link.click()
    time.sleep(5)