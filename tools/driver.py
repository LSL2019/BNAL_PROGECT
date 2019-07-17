from appium import webdriver


class GetDriver:
    _driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if not cls._driver:
            # server 启动参数
            desired_caps = {}  # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'  # app信息
            desired_caps['appPackage'] = 'com.yunmall.lc'
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.WebViewActivity'
            # desired_caps['appPackage'] = 'com.android.settings'
            # desired_caps['appActivity'] = '.Settings'
            # 中文
            # desired_caps['unicodeKeyboard'] = True
            # desired_caps['resetKeyboard'] = True
            # 获取toast消息
            desired_caps['automationName'] = "Uiautomator2"
            cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
