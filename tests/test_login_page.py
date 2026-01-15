import allure
import pytest
from allure_commons.types import AttachmentType

from pages.login_page import LoginPage
import time


@allure.feature('user_login')
@allure.story('Enter valid login and password')
@allure.severity('blocker')
@pytest.mark.smoke
def test_log_in(driver):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(driver, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.login_btn()
    time.sleep(5)
    with allure.step('Make screenshot'):
        allure.attach(driver.get_screenshot_as_png(), name='result_profile_p_opened',
                      attachment_type=AttachmentType.PNG)
    # driver.save_screenshot('result_submit.png')
    profile = page.find_profile()
    assert profile
