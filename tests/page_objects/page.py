from hamcrest import assert_that
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from tests.custom_matchers.wait_for_matcher import waits_to_have


class Page:

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    def go_to_page_url(self):
        self.driver.get(self.url)

    def send_keys_to_element(self, locator, keys, override=False):
        assert_that(self, waits_to_have(ec.element_to_be_clickable, locator))
        element = self.driver.find_element(*locator)
        if override:
            element.send_keys(Keys.CONTROL, "a")
        element.send_keys(keys)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_clickable(self, locator):
        assert_that(self, waits_to_have(ec.element_to_be_clickable, locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()