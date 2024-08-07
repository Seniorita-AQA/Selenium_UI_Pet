import time

import pytest

from pages.profile_page import ProfilePage


@pytest.mark.functional
def test_create_cat(auth_user, browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_create_cat()
    time.sleep(5)
    browser.save_screenshot('create_new_pet.png')


@pytest.mark.functional
def test_delete_pet(auth_user, browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet()
    time.sleep(5)
    browser.save_screenshot('deleted_pet.png')


@pytest.mark.functional
def test_delete_account(auth_user, browser):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_account()
    time.sleep(5)
    browser.save_screenshot('deleted_account.png')


@pytest.mark.functional
def test_quit(auth_user, browser):
    browser = auth_user
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_quit()
    time.sleep(5)
    browser.save_screenshot('quit.png')
