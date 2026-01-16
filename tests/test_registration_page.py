import time

import pytest

from pages.registration_page import RegistrationPage


@pytest.mark.smoke
def test_registration_user(driver):
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(driver, link)
    page.open()
    page.registration_user()
    driver.save_screenshot('result_registered_user.png')

