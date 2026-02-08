import pytest
from driver_factory import create_driver
from pages.login_page import LoginPage
from config import SUPPORTED_BROWSERS, OPTIONAL_BROWSERS, DEFAULT_BROWSER


@pytest.fixture(scope="class", params=DEFAULT_BROWSER)
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
    page.log_in_user()
    yield driver




