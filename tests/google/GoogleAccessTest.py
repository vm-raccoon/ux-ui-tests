from classes.BaseTest import BaseTest


class GoogleAccessTest(BaseTest):

    def __init__(self):
        print('Run GoogleAccessTest')

    def run(self):
        self.run_chrome()
        self.run_firefox()

    def run_chrome(self):
        chrome = self.get_chrome_driver()
        chrome.get('https://google.com.ua')
        print("Google page title (chrome):", chrome.title)
        chrome.quit()

    def run_firefox(self):
        firefox = self.get_firefox_driver()
        firefox.get('https://google.com.ua')
        print("Google page title (firefox):", firefox.title)
        firefox.quit()
