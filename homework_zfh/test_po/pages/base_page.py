from time import sleep

import pytest
import json
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.__cookie__login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie__login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流方式打开cookie
        with open("../../test_web_selenium/cookie.json", "r") as f:
            # 读取cookies
            cookies = json.load(f)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        # self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
