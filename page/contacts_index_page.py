import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactsIndexPage(BaseAction):

    # 新建联系人图标
    # add_contact_icon = By.ID, "com.android.contacts:id/floating_action_button"
    add_contact_icon = By.XPATH, "//*[@content-desc='添加新联系人']"

    # 点击新增联系人图标
    @allure.step(title="点击新增联系人图标")
    def click_add_contact_icon(self):
        self.click(self.add_contact_icon)
