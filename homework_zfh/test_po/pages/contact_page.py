"""
1.通讯录页面，可以点击添加成员
2.可以点击添加部门
"""
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.remote import webelement


from homework_zfh.test_po.pages.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '.js_add_member').click()
        from homework_zfh.test_po.pages.member_page import MemberPage
        return MemberPage(self.driver)

    # 添加部门
    def goto_add_dept(self):
        self.find(By.CSS_SELECTOR, '.js_create_dropdown').click()
        self.find(By.CSS_SELECTOR,'.js_create_party').click()

        from homework_zfh.test_po.pages.adept_page import AdeptPage
        return AdeptPage(self.driver)

    def get_list(self):
        # 返回通讯录的人员信息
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, "li[role=treeitem].jstree-node.js_editable.jstree-leaf.jstree-last")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(str.strip(webelement.text))
        return name_list
