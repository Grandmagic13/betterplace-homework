import operator

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.library.number.ordering_comparison import OrderingComparison
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants import DEFAULT_WAIT_TIME
from tests.custom_matchers.wait_for_matcher import WaitsToHave
from selenium.webdriver.support import expected_conditions as ec


class HasNumberOfElementsGreaterThan(BaseMatcher):

    def __init__(self, lower_boundary, locator):
        self.lower_boundary = lower_boundary
        self.locator = locator
        self.is_mismatch_due_to_timeout = False

    def _matches(self, page_object):
        self.page_object = page_object
        self.expected_condition = ec.presence_of_all_elements_located
        self.waits_to_have_matcher = WaitsToHave(ec.presence_of_all_elements_located, self.locator)
        if self.waits_to_have_matcher._matches(page_object):
            self.element_list_length = len(page_object.find_elements(self.locator))
            greater_than_matcher = OrderingComparison(self.lower_boundary, operator.gt, "greater than")
            return greater_than_matcher._matches(self.element_list_length)
        self.is_mismatch_due_to_timeout = True
        return False

    def describe_to(self, description):
        expected_message = "Element list located via '{0}' with length greater than <{1}>"
        description.append_text(expected_message.format(self.locator, self.lower_boundary))

    def describe_mismatch(self, json_object, description):
        if self.is_mismatch_due_to_timeout:
            page_object_class = self.page_object.__class__.__name__
            expected_condition_name =  self.expected_condition.__name__
            expected_message = "Page ({0}) didn't meet condition '{1}' for locator: {2}"
            description.append_text(expected_message.format(page_object_class, expected_condition_name, self.locator))
        else:
            description.append_text("Element list length was <{0}>".format(self.element_list_length))


def has_number_of_elements_greater_than(lower_boundary, locator):
    return HasNumberOfElementsGreaterThan(lower_boundary, locator)
