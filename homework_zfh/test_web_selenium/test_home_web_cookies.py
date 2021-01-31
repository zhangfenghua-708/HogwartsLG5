import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


# 使用cookies，实现企业微信登录并点击客户联系
class TestWechat:
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # 获取cookie
        cookies = self.driver.get_cookies()
        print(cookies)
        # 以文件流形式打开文件
        # with open("cookie.json", "w+") as f:
        #     # 存储cookie到cookie.json
        #      json.dump(cookies, f)
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流形式打开文件
        with open("cookie.json", "r") as i:
            # 读取cookies
            cookies = json.load(i)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()