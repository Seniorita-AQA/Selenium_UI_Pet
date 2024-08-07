from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]/span[1]')
    DDOWN_FIELD = (By.ID, 'typesSelector')
    FILTER_CAT = (By.XPATH, '//*[@id="typesSelector"]')
    FILTER_NAME = (By.ID, 'petName')
    DETAILS_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(1) .p-button-label')
    THUMBS_UP_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(1) .product-grid-item-bottom .pi')
    COMMENTS_FIELD = (By.XPATH, "//div[@id='app']/main/div[2]/div/div/div[3]/form/div/div/div[2]/div")
    SAVE_COMMENT_BTN = (By.XPATH, "//div[@id='app']/main/div[2]/div/div/div[3]/form/div/button/span[2]")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    CREATE_CAT = (By.CLASS_NAME, 'pi-plus')
    INPUT_PET_NAME = (By.ID, 'name')
    DDOWN_OPEN = (By.ID, 'typeSelector')
    CHOOSE_PET_TYPE = (By.XPATH, "//li[@aria-label='cat']")
    CLICK_ON_SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CLICK_ON_CHOOSE_AVA_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/span[2]')
    CHOOSE_PIK = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    CLICK_ON_UPLOADED_BTN = (By.XPATH, '//div[@id="app"]/main/div/div/div[2]/div[2]/div/span')

    DELETE_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div/div/div/div[2]/button[2]/span[2]")
    DELETE_YES = (By.CSS_SELECTOR, '.p-confirm-popup-accept > .p-button-label')

    DELETE_ACC_BTN = (By.CSS_SELECTOR, '.p-button-icon-only > .pi-trash')
    CONFIRM_DELETE_ACC_YES = (By.XPATH, '//div[3]/div[2]/button[2]/span')

    QUIT_BTN = (By.CSS_SELECTOR,".p-menuitem:nth-child(2) .p-menuitem-text")


class RegistrationPageLocators:
    LOGIN_FIELD = (By.ID, 'login')
    PASS_FIELD = (By.CSS_SELECTOR, '#password > .p-inputtext')
    CONFIRM_PASS = (By.CSS_SELECTOR, '#confirm_password > .p-inputtext')
    SUBMIT_BTN_REGISTRATION = (By.CSS_SELECTOR, '.p-button-label')



