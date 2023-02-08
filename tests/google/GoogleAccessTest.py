from classes.BaseTest import BaseTest


class GoogleAccessTest(BaseTest):

    def __init__(self):
        print('Run GoogleAccessTest')

    def run(self):
        driver = self.get_chrome_driver()
        driver.get('https://google.com.ua')
        print("Google page title:", driver.title)
        driver.quit()
