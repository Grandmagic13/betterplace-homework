from hamcrest import assert_that
from selenium.webdriver import ActionChains

from tests.custom_matchers.wait_for_matcher import waits_to_have
from selenium.webdriver.support import expected_conditions as ec


class SmartClientPage:

    def __init__(self, driver):
        self.base_page = "http://www.smartclient.com/smartgwt/showcase"
        self.driver = driver

    def go_to_page_url(self):
        self.driver.get(self.base_page)

    def send_keys_to_element(self, locator, keys):
        assert_that(self, waits_to_have(ec.element_to_be_clickable, locator))
        element = self.driver.find_element(*locator)
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

    def scroll_down_dropdown(self, scroll_thumb, y_offset):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(scroll_thumb, 0, y_offset)
        actions.perform()


def create_subpage_url(base_page, sub_address):
    return "{0}/{1}".format(base_page, sub_address)


def generate_combo_box_xpath(label):
    return "//label[text()='{0}']/following::span[@class='comboBoxItemPicker']".format(label)
