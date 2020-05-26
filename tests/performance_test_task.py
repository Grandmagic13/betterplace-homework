import time
import unittest

from hamcrest import assert_that, less_than_or_equal_to
from selenium import webdriver

from tests.constants import DEFAULT_WAIT_TIME
from tests.page_objects.amazon import AmazonPage


class PerformanceTest(unittest.TestCase):
    def test_search_performance(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(DEFAULT_WAIT_TIME)
        page = AmazonPage(self.driver)
        page.go_to_page_url()
        page.search_for_item("Playstation 4")
        response_time = page.measure_response_time_in_milliseconds()
        assert_that(response_time, less_than_or_equal_to(1000))