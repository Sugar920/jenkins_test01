import allure
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContacts:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize("args", analyze_file("test_contacts_data.yaml", "test_contacts"))
    def test_contacts(self, args):
        name = args["name"]
        tel = args["tel"]
        # 点击新增联系人
        self.page.contacts_index.click_add_contact_icon()
        # 输入姓名
        self.page.add_contact.input_name(name)
        # 输入电话
        self.page.add_contact.input_tel(tel)
        # 点击返回
        self.page.add_contact.click_back()

        # 断言：获取的name是否 name一致
        assert name == self.page.saved_contact.get_name_title()
