import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):

    # 姓名输入框
    name = By.XPATH, "//*[@text='姓名']"
    # 电话输入框
    tel = By.XPATH, "//*[@text='电话']"

    # 输入姓名
    @allure.step(title="输入姓名")
    def input_name(self, name):
        allure.attach("输入", name, allure.attachment_type.TEXT)
        self.input(self.name, name)

    # 输入电话
    @allure.step(title="输入电话")
    def input_tel(self, tel):
        allure.attach("输入", tel, allure.attachment_type.TEXT)
        self.input(self.tel, tel)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attachment_type.PNG)

    # 点击返回
    @allure.step(title="点击返回")
    def click_back(self):
        self.press_back()