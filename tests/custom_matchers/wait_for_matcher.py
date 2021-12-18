from hamcrest.core.base_matcher import BaseMatcher
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants import DEFAULT_WAIT_TIME


class WaitsToHave(BaseMatcher):

    def __init__(self, expected_condition, locator):
        self.expected_condition = expected_condition
        self.locator = locator

    def _matches(self, page_object):
        self.page_object = page_object
        try:
            WebDriverWait(page_object.driver, DEFAULT_WAIT_TIME).until(lambda x: self.expected_condition(self.locator))
            return True
        except TimeoutException:
            return False

    def describe_to(self, description):
        page_object_class = self.page_object.__class__.__name__
        expected_condition_name =  self.expected_condition.__name__
        expected_message = "Page ({0}) to meet condition '{1}' for locator: {2}"
        description.append_text(expected_message.format(page_object_class, expected_condition_name, self.locator))

    def describe_mismatch(self, json_object, description):
        description.append_text("Condition has timed out (timeout: {0} seconds)".format(DEFAULT_WAIT_TIME))


def waits_to_have(expected_condition, locator):
    return WaitsToHave(expected_condition, locator)
