import pytest
from driver_factory import create_driver
from pages.login_page import LoginPage


@pytest.fixture(scope='class', params=['chrome'])
def driver(request):
    driver = create_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def auth_user(driver):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(driver, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.login_btn()
    yield driver




