from selenium.webdriver import Keys

from .base_page import BasePage

from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def filter_by_pet_type_cat(self):
        ddown_field = self.browser.find_element(*MainPageLocators.DDOWN_FIELD)
        ddown_field.click()
        choose_cat = self.browser.find_element(*MainPageLocators.FILTER_CAT)
        choose_cat.click()

    def filter_by_pet_name(self):
        click_on_field_name = self.browser.find_element(*MainPageLocators.FILTER_NAME)
        click_on_field_name.click()
        type_pet_name = self.browser.find_element(*MainPageLocators.FILTER_NAME)
        type_pet_name.send_keys('Tipsy')
        type_pet_name.send_keys(Keys.ENTER)

    def show_pet_details(self):
        click_on_details_btn = self.browser.find_element(*MainPageLocators.DETAILS_BTN)
        click_on_details_btn.click()

    def like_pet_card(self):
        click_on_thumbs_up_btn = self.browser.find_element(*MainPageLocators.THUMBS_UP_BTN)
        click_on_thumbs_up_btn.click()

    def add_comment(self):
        click_on_details_btn = self.browser.find_element(*MainPageLocators.DETAILS_BTN)
        click_on_details_btn.click()
        click_on_comments_field = self.browser.find_element(*MainPageLocators.COMMENTS_FIELD)
        click_on_comments_field.click()
        click_on_comments_field.send_keys('I love this breed of pet')
        click_on_save_comment_btn = self.browser.find_element(*MainPageLocators.SAVE_COMMENT_BTN)
        click_on_save_comment_btn.click()
