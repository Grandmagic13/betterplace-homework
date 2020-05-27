import concurrent.futures
import unittest
from concurrent.futures import as_completed

from hamcrest import assert_that, less_than_or_equal_to, only_contains
from selenium import webdriver

from tests.constants import DEFAULT_WAIT_TIME
from tests.page_objects.amazon import AmazonPage


class PerformanceTest(unittest.TestCase):
    def test_search_performance(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            number_of_threads = 10
            futures = [executor.submit(self.measure_search) for i in range(number_of_threads)]
            response_times = [completed.result() for completed in as_completed(futures)]
        assert_that(response_times, only_contains(less_than_or_equal_to(1000)))

    def measure_search(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(DEFAULT_WAIT_TIME)
        page = AmazonPage(driver)
        page.go_to_page_url()
        page.search_for_item("Playstation 4")
        return page.measure_response_time_in_milliseconds()
