from homework_zfh.test_po.pages.main_page import MainPage


class TestAdddept:

    def setup_class(self):
        # 实例化MainPage类
        self.main = MainPage()

    def test_add_dept(self):
        # 1.通讯页面，输入部门名称，选择所属部门，点击保存
        self.main.goto_contact().goto_add_dept().add_dept("测试部2")
        result = self.main.goto_contact().get_list()
        assert "测试部2" in result