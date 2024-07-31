from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys("user1@gmail.com")

    def enter_pass(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys("123zxcv")

    def login_btn(self):
        click_login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        click_login_btn.submit()
