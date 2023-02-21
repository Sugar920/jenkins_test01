from appium import webdriver


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 不重置
    desired_caps['noReset'] = True
    # 中文参数
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app信息
    # desired_caps['appPackage'] = 'com.android.settings'
    #     # desired_caps['appActivity'] = '.Settings'
    # desired_caps['appPackage'] = 'com.android.mms'
    # desired_caps['appActivity'] = '.ui.ConversationList'

    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
