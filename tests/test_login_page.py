import pytest

from pages.login_page import LoginPage
import time


@pytest.mark.smoke
def test_log_in(browser):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.login_btn()
    time.sleep(5)
    browser.save_screenshot('result_submit.png')















