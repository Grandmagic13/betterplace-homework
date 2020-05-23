import time
import unittest

from hamcrest import assert_that
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from test_automation_task.constants import *
from test_automation_task.custom_matchers.wait_for_matcher import waits_to_have
from test_automation_task.page_objects.featured_file_filtering_page import FeaturedFileFilteringPage


class Exercises(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(DEFAULT_WAIT_TIME)

    def test_exercise_1(self):
        # Exercise 1.
        # http://www.smartclient.com/smartgwt/showcase/#featured_tile_filtering

        page = FeaturedFileFilteringPage(self.driver)
        page.go_to_page_url()

        # Fill fields
        # 1.	Animal set using letter „a”

        page.send_keys_to_animal_input("a")

        # 2.	Max life span set to  40
        # 3.	Sort order by „Life Span”
        # 4.	Select checkbox  to Ascending
        #
        # Assert that results contains more than 12 items

        # TODO delete, only for observation purposes
        time.sleep(5.0)
