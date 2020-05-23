from hamcrest import assert_that
from selenium.webdriver.common.by import By

from test_automation_task.custom_matchers.wait_for_matcher import waits_to_have
from selenium.webdriver.support import expected_conditions as ec


class SmartClientPage:

    def __init__(self, driver):
        self.base_page = "http://www.smartclient.com/smartgwt/showcase"
        self.driver = driver

    def go_to_page_url(self):
        self.driver.get(self.base_page)

    def send_keys_to_xpath(self, xpath, keys):
        locator = (By.XPATH, xpath)
        assert_that(self, waits_to_have(ec.element_to_be_clickable, locator))
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(keys)
