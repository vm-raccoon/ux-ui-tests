from selenium import webdriver
import os


def get_chrome(options={}):
    debug = options.get("debug") or False
    options = webdriver.ChromeOptions()
    if not debug:
        options.add_argument('--headless')
    driver = webdriver.Chrome(
        options=options,
        executable_path=r"./webdrivers/chromedriver"
    )
    return driver


def get_firefox(options={}):
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


def get_edge(options={}):
    debug = options.get("debug") or False
    driver = webdriver.Edge(
        # options=options,
        executable_path=r"./webdrivers/msedgedriver"
    )
    return driver


def set_size(driver, size):
    driver.set_window_size(size['width'], size['height'])
