import time
import pytest
from pages.main_page import MainPage

@pytest.mark.regression
class TestMainPage:

    def test_go_to_login_page(self, driver):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        time.sleep(5)
        driver.save_screenshot('result_login_page.png')


    def test_filter_by_type(self, driver):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.filter_by_pet_type_cat()
        time.sleep(5)
        driver.save_screenshot('result_filter_by_cat.png')


    def test_filter_by_pet_name(self, driver):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.filter_by_pet_name()
        time.sleep(5)
        driver.save_screenshot('result_filter_by_name.png')


    def test_show_pet_details(self, driver):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.show_pet_details()
        time.sleep(5)
        driver.save_screenshot('result_show_pet_details.png')


    def test_like_pet_card(self, driver, auth_user):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.like_pet_card()
        time.sleep(5)
        driver.save_screenshot('result_like_pet_card.png')


    def test_add_comment(self, driver, auth_user):
        link = 'http://34.141.58.52:8080/#/'
        page = MainPage(driver, link)
        page.open()
        page.like_pet_card()
        time.sleep(5)
        driver.save_screenshot('result_add_comment.png')