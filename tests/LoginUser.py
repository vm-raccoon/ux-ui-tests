from classes.BaseTest import BaseTest
from tools import Browser
from classes.ui.window_size import Screen
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginUser(BaseTest):

    def __init__(self):
        print('Run', self.__module__)
        self.driver = Browser.get_chrome({'debug': True})
        self.wait = WebDriverWait(self.driver, 15)

    def __del__(self):
        self.driver.quit()

    def run(self):
        Browser.set_size(self.driver, Screen.FHD)
        self.login()
        self.driver.get('https://breezy.ua/smartphone')
        self.logout()

    def login(self):
        self.driver.get('https://breezy.ua')
        self.driver.find_element_by_css_selector('.header [data-target="login_modal"]').click()
        self.driver.find_element_by_css_selector('#login_form input[name="email"]').send_keys('email')
        self.driver.find_element_by_css_selector('#login_form input[name="password"]').send_keys('password')
        self.driver.find_element_by_css_selector('#login_form .btn[data-func="login"]').click()
        self.wait.until(EC.url_to_be('https://breezy.ua/cabinet/profile'))
        print(self.driver.current_url)

    def logout(self):
        self.driver.get('https://breezy.ua/cabinet/profile')
        self.driver.find_element_by_css_selector('.profile_menu_list a[data-action-logout]').click()
        self.wait.until(EC.url_matches('https://breezy.ua'))
        print(self.driver.current_url)
