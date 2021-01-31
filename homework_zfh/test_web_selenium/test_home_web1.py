import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestWechat:
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    # def teardown_method(self):
    #     self.driver.quit()

    def test_wechat(self):
        # self.driver.get("https://work.weixin.qq.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
