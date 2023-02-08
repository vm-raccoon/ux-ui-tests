from abc import abstractmethod
from selenium import webdriver
import os


class BaseTest:

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    def get_chrome_driver(options={}):
        debug = options.get("debug") or False
        options = webdriver.ChromeOptions()
        if not debug:
            options.add_argument('--headless')
        driver = webdriver.Chrome(
            options=options,
            executable_path=r"./webdrivers/chromedriver"
        )
        return driver

    @staticmethod
    def get_firefox_driver(options={}):
        debug = options.get("debug") or False
        options = webdriver.FirefoxOptions()
        options.add_argument('--log-level=off')
        if not debug:
            options.add_argument('--headless')
        driver = webdriver.Firefox(
            service_log_path=os.devnull,
            options=options,
            executable_path=r"./webdrivers/geckodriver"
        )
        return driver
