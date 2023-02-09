from classes.BaseTest import BaseTest
from tools import Browser
from classes.ui.window_size import BreakPoint
from classes.ui.window_size import Screen


class GoogleAccessTest(BaseTest):

    def __init__(self):
        print('Run GoogleAccessTest')
        self.default_browser_options = {
            'debug': True,
        }

    def run(self):
        self.run_chrome()
        self.run_firefox()

    def run_chrome(self):
        chrome = Browser.get_chrome(self.default_browser_options)
        Browser.set_size(chrome, BreakPoint.MOBILE)
        chrome.get('https://google.com.ua')
        print("Google page title (chrome):", chrome.title)
        chrome.quit()

    def run_firefox(self):
        firefox = Browser.get_firefox(self.default_browser_options)
        Browser.set_size(firefox, Screen.FHD)
        firefox.get('https://google.com.ua')
        print("Google page title (firefox):", firefox.title)
        firefox.quit()
