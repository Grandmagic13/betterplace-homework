from selenium.webdriver.common.by import By

from tests.page_objects.page import Page


class CharityPage(Page):

    COOKIES_OKAY_BUTTON_LOCATOR = (By.XPATH, "//div[@class='cookie-content-wrapper']//button[text()='Okay!']")

    def __init__(self, driver, toggle_bugged_page=False):
        postfix = "?force-bug=1" if toggle_bugged_page else ""
        super(CharityPage, self).__init__(driver, url="https://www.bp42.com/de/donate/platform/projects/1114{}".format(postfix))

    def close_cookie_banner(self):
        self.click(self.COOKIES_OKAY_BUTTON_LOCATOR)



