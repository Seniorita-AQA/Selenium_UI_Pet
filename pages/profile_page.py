from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def go_to_create_cat(self):
        click_plus_btn = self.browser.find_element(*ProfilePageLocators.CREATE_CAT)
        click_plus_btn.click()
        input_pet_name = self.browser.find_element(*ProfilePageLocators.INPUT_PET_NAME)
        input_pet_name.send_keys("Margo")
        ddown_open = self.browser.find_element(*ProfilePageLocators.DDOWN_OPEN)
        ddown_open.click()
        choice_pet_type = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE)
        choice_pet_type.click()
        click_on_submit_btn = self.browser.find_element(*ProfilePageLocators.CLICK_ON_SUBMIT_BUTTON)
        click_on_submit_btn.click()
        choose_ava_btn = self.browser.find_element(*ProfilePageLocators.CLICK_ON_CHOOSE_AVA_BTN)
        choose_ava_btn.click()
        choose_ava = self.browser.find_element(*ProfilePageLocators.CHOOSE_PIK)
        choose_ava.send_keys(r'C:\Users\User\PycharmProjects\Selenium_UI_Pet\pictures\Cat.jpeg')
        add_ava = self.browser.find_element(*ProfilePageLocators.CLICK_ON_UPLOADED_BTN)
        add_ava.click()

    def go_to_edit_pet(self):
        click_on_edit_btn = self.browser.find_element(*ProfilePageLocators.CLICK_ON_EDIT_BTN)
        click_on_edit_btn.click()
        input_new_pet_name = self.browser.find_element(*ProfilePageLocators.INPUT_NEW_PET_NAME)
        input_new_pet_name.click()
        input_new_pet_name.clear()
        input_new_pet_name.send_keys("Tom")
        ddown_type_open = self.browser.find_element(*ProfilePageLocators.DDOWN_TYPE_OPEN)
        ddown_type_open.click()
        choose_new_pet_type = self.browser.find_element(*ProfilePageLocators.CHOOSE_NEW_PET_TYPE)
        choose_new_pet_type.click()
        click_on_save_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BTN)
        click_on_save_btn.click()

    def go_to_delete_pet(self):
        click_on_delete_btn = self.browser.find_element(*ProfilePageLocators.DELETE_BTN)
        click_on_delete_btn.click()
        confirm_delete_yes = self.browser.find_element(*ProfilePageLocators.DELETE_YES)
        confirm_delete_yes.click()

    def go_to_delete_account(self):
        click_on_delete_acc = self.browser.find_element(*ProfilePageLocators.DELETE_ACC_BTN)
        click_on_delete_acc.click()
        confirm_delete_acc_yes = self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_ACC_YES)
        confirm_delete_acc_yes.click()

    def go_to_quit(self):
        quit_btn = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_btn.click()