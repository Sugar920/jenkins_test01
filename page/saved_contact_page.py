import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):

    # 姓名框
    name_title = By.ID, "com.android.contacts:id/large_title"

    # 获取姓名
    @allure.step(title="获取姓名")
    def get_name_title(self):
        return self.get_text(self.name_title)
