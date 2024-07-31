import time
from utils.generator import generate_random_email, generate_random_password
from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def registration_user(self):
        login_field = self.browser.find_element(*RegistrationPageLocators.LOGIN_FIELD)

        email = generate_random_email()
        login_field.click()
        login_field.send_keys(email)
        time.sleep(5)

        pass_field = self.browser.find_element(*RegistrationPageLocators.PASS_FIELD)
        pass_field.submit()

        password = generate_random_password()
        pass_field.send_keys(password)
        time.sleep(5)

        confirm_pass_field = self.browser.find_element(*RegistrationPageLocators.CONFIRM_PASS)
        confirm_pass_field.submit()
        confirm_pass_field.send_keys(password)
        time.sleep(5)

        click_on_submit_btn = self.browser.find_element(*RegistrationPageLocators.SUBMIT_BTN_REGISTRATION)
        click_on_submit_btn.submit()
        time.sleep(5)


