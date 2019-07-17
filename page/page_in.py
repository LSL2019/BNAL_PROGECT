from page.page_login import PageLogin
from tools.driver import GetDriver


class PageIn(object):
    driver = GetDriver().get_driver()

    # 获取pageLogin对象
    def page_in_get_page_login(self):
        return PageLogin(self.driver)
