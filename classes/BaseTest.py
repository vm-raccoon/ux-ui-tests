from abc import abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BaseTest:

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    def get_chrome_driver(options={}):
        debug = options.get("debug") or False
        options = ChromeOptions()
        if not debug:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options, executable_path=r"./webdrivers/chromedriver")
        return driver
