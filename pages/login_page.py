from .base_page import BasePage
from .locators import LoginPageLocators
from config import EMAIL, PASSWORD

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def log_in_user(self):
        wait = WebDriverWait(self.driver, 10)

        # Login
        login_email = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL)
        )
        login_email.send_keys()

        # Password
        login_password = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_PASS)
        )
        login_password.send_keys()

        # Submit
        click_login_btn = wait.until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BTN)
        )
        click_login_btn.submit()

        # User is logged in
        profile = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE)
        )

        return profile
