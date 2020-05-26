from selenium.webdriver.common.by import By

from tests.page_objects.page import Page


class AmazonPage(Page):
    SEARCHBOX_LOCATOR = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//input[@class='nav-input' and @value='Go']")

    def __init__(self, driver):
        super(AmazonPage, self).__init__(driver, url="https://www.amazon.com/")

    def search_for_item(self, item):
        self.send_keys_to_element(self.SEARCHBOX_LOCATOR, item)
        self.click(self.SEARCH_BUTTON)

    def measure_response_time_in_milliseconds(self):
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        return domComplete - responseStart