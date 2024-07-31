from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]/span[1]')
    DDOWN_FIELD = (By.ID, 'typesSelector')
    FILTER_CAT = (By.ID, 'pv_id_2_1')
    FILTER_NAME = (By.ID, 'petName')
    DETAILS_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(1) .p-button-label')
    THUMBS_UP_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(1) .product-grid-item-bottom .pi')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    CREATE_CAT = (By.CLASS_NAME, 'pi-plus')
    INPUT_PET_NAME = (By.XPATH, "//*[@id='name']")
    DDOWN_OPEN = (By.ID, 'typeSelector')
    CHOOSE_PET_TYPE = (By.XPATH, '//*[@id="pv_id_4_1"]')
    CLICK_ON_SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CLICK_ON_CHOOSE_AVA_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/span[2]')
    CHOOSE_PIK = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    CLICK_ON_UPLOADED_BTN = (By.XPATH, '//div[@id="app"]/main/div/div/div[2]/div[2]/div/span')

    CLICK_ON_EDIT_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(1) .p-button:nth-child(1) > .p-button-label')
    INPUT_NEW_PET_NAME = (By.XPATH, '//*[@id="name"]')
    DDOWN_TYPE_OPEN = (By.ID, 'typeSelector')
    CHOOSE_NEW_PET_TYPE = (By.XPATH, '//*[@id="pv_id_4_3"]')
    SAVE_BTN = (By.CSS_SELECTOR, '.p-button-success > .p-button-label')

    # DELETE_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(4) .p-button-danger > .p-button-label')
    DELETE_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div/div/div/div[2]/button[2]/span[2]")
    DELETE_YES = (By.CSS_SELECTOR, '.p-confirm-popup-accept > .p-button-label')

    DELETE_ACC_BTN = (By.CSS_SELECTOR, '.p-button-icon-only > .pi-trash')
    CONFIRM_DELETE_ACC_YES = (By.XPATH, '//div[3]/div[2]/button[2]/span')

    QUIT_BTN = (By.XPATH, "//div[@id='app']/header/div/ul/li[2]/a/span[2]")


class RegistrationPageLocators:
    LOGIN_FIELD = (By.ID, 'login')
    PASS_FIELD = (By.CSS_SELECTOR, '#password > .p-inputtext')
    CONFIRM_PASS = (By.CSS_SELECTOR, '#confirm_password > .p-inputtext')
    SUBMIT_BTN_REGISTRATION = (By.CSS_SELECTOR, '.p-button-label')



