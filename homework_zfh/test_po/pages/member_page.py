"""
1.添加成员页面，点击保存，返回到通讯录页面
"""
from selenium.webdriver.common.by import By

from homework_zfh.test_po.pages.base_page import BasePage



class MemberPage(BasePage):
    __username = (By.ID, "username")

    def add_member(self,name,account,phone):
        # 输入成员信息，点击保存
        self.find(By.ID,'username').send_keys(name)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        from homework_zfh.test_po.pages.contact_page import ContactPage
        return ContactPage(self.driver)
