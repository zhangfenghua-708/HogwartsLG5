"""
1.添加部门页面，点击保存可以成功添加部门，并返回通讯录页面，验证是否添加成功
"""
from selenium.webdriver.common.by import By

from homework_zfh.test_po.pages.base_page import BasePage



class AdeptPage(BasePage):
    def add_dept(self,name):
        # 添加部门信息
        self.find(By.NAME,'name').send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        # 选择所属部门
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851024242207_anchor']").click()
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()
        from homework_zfh.test_po.pages.contact_page import ContactPage
        return ContactPage(self.driver)