from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService

import sys

"""Paths to local driver binaries for Win"""
CHROME_DRIVER_PATH = r"C:\Drivers\chromdriver\chromedriver.exe"
FIREFOX_DRIVER_PATH = r"C:\Drivers\geckodriver-v0.36.0-win64\geckodriver.exe"
EDGE_DRIVER_PATH = r"C:\Drivers\edgedriver_win64\msedgedriver.exe"

"""Path to local driver for testing on Chrome browser on MacOS"""
CHROME_DRIVER_PATH_MACOS = r"/opt/homebrew/bin/chromedriver"


def create_driver(browser: str):

    browser = browser.lower()

    if browser == "chrome":
        service = ChromeService(executable_path=CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

    elif browser == "chrome":
        service = ChromeService(executable_path=CHROME_DRIVER_PATH_MACOS)
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FirefoxService(executable_path=FIREFOX_DRIVER_PATH)
        driver = webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(executable_path=EDGE_DRIVER_PATH)
        driver = webdriver.Edge(service=service)

    elif browser == "safari":
        if sys.platform != "darwin":
            raise RuntimeError("Safari can be run only on macOS")
        driver = webdriver.Safari(service=SafariService())

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver

