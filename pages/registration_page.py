from utils.generator import generate_random_email, generate_random_password
from .base_page import BasePage
from .locators import RegistrationPageLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):

    def registration_user(self):
        wait = WebDriverWait(self.driver, 10)

        # Email
        email_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FIELD)
        )
        email = generate_random_email()
        email_field.send_keys(email)

        # Password
        pass_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASS_FIELD)
        )
        password = generate_random_password()
        pass_field.send_keys(password)

        # Confirm password
        confirm_pass_field = wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.CONFIRM_PASS)
        )
        confirm_pass_field.send_keys(password)

        # Submit
        wait.until(
            EC.presence_of_element_located(
                RegistrationPageLocators.SUBMIT_BTN_REGISTRATION
            )
        ).submit()

        return email, password



