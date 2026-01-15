# from selenium import webdriver
#
#
# def create_driver(browser):
#     if browser == "chrome":
#         return webdriver.Chrome()
#     elif browser == "firefox":
#         return webdriver.Firefox()
#     elif browser == "edge":
#         return webdriver.Edge()
#     elif browser == "safari":
#         return webdriver.Safari()
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


# --- Paths to local driver binaries ---
CHROME_DRIVER_PATH = r"C:\Drivers\chromdriver\chromedriver.exe"
FIREFOX_DRIVER_PATH = r"C:\Drivers\geckodriver-v0.36.0-win64\geckodriver.exe"
EDGE_DRIVER_PATH = r"C:\Drivers\edgedriver_win64\msedgedriver.exe"


def create_driver(browser: str):

    browser = browser.lower()

    if browser == "chrome":
        service = ChromeService(executable_path=CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FirefoxService(executable_path=FIREFOX_DRIVER_PATH)
        driver = webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(executable_path=EDGE_DRIVER_PATH)
        driver = webdriver.Edge(service=service)

    elif browser == "safari":      # Safari driver is built into macOS
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver

