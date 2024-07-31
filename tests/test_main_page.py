import time

import pytest

from pages.main_page import MainPage


@pytest.mark.regression
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)
    browser.save_screenshot('result_log_page.png')


@pytest.mark.regression
def test_filter_by_type(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_type_cat()
    time.sleep(5)
    browser.save_screenshot('result_filter_by_cat.png')


@pytest.mark.regression
def test_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name()
    time.sleep(5)
    browser.save_screenshot('result_filter_by_name.png')


@pytest.mark.regression
def test_show_pet_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.show_pet_details()
    time.sleep(5)
    browser.save_screenshot('result_show_pet_details.png')


@pytest.mark.regression
def test_like_pet_card(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.like_pet_card()
    time.sleep(5)
    browser.save_screenshot('result_like_pet_card.png')
