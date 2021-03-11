import time

import pytest
from selenium.webdriver.common.by import By


from homework_zfh.test_po.pages.base_page import BasePage
from homework_zfh.test_po.pages.contact_page import ContactPage
from homework_zfh.test_po.pages.import_contact_page import ImportcontactPage

"""
1.企业微信主页面，可以点击通讯录
2.可以添加成员
3.可以点击导入通讯录，跳转到导入通讯录页面
"""


class MainPage(BasePage):
    def goto_contact(self):
        time.sleep(1)
        self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)

    def add_member(self):
        self.find(By.CSS_SELECTOR,'.ww_indexImg_AddMember').click()
        from homework_zfh.test_po.pages.member_page import MemberPage
        return MemberPage(self.driver)

    def import_contact(self):
        self.find(By.CSS_SELECTOR,'index_service_cnt_item_title').click()
        return ImportcontactPage(self.driver)