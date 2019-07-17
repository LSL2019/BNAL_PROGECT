from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入内容
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入内容
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 获取toast消息
    def base_get_toast(self, msg):
        loc = By.XPATH, '//*[contains(@text,"{}")]'.format(msg)
        return self.base_find(loc, timeout=30, poll=0.2).text

    # 元素拖拽方法
    def base_drag_and_drop(self, start_loc, end_loc):
        start_el = self.base_find(start_loc)
        end_el = self.base_find(end_loc)
        self.driver.drag_and_drop(start_el, end_el)

    # 截图方法
    def base_get_img(self):
        return self.driver.get_screenshot_as_file("./image/fail.png")
