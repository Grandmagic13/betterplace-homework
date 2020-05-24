import time
import unittest

from hamcrest import assert_that, is_, greater_than
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_automation_task.constants import *
from test_automation_task.custom_matchers.has_number_of_elements_greater_than import has_number_of_elements_greater_than
from test_automation_task.custom_matchers.wait_for_matcher import waits_to_have
from test_automation_task.page_objects.featured_dropdown_grid_category_page import FeaturedDropdownGridCategoryPage
from test_automation_task.page_objects.featured_file_filtering_page import FeaturedFileFilteringPage
from selenium.webdriver.support import expected_conditions as ec


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

        page.set_age_slider_to(40)

        # 3.	Sort order by „Life Span”

        page.select_sort_order(FeaturedFileFilteringPage.SORT_ORDER_OPTION_LIFE_SPAN)

        # 4.	Select checkbox  to Ascending

        page.tick_ascending_checkbox()

        # Assert that results contains more than 12 items

        assert_that(page, has_number_of_elements_greater_than(12, FeaturedFileFilteringPage.TILE_SORTED_HITS_LOCATOR))

    def test_exercise_2(self):
        # Exercise 2.
        # http://www.smartclient.com/smartgwt/showcase/#featured_dropdown_grid_category

        page = FeaturedDropdownGridCategoryPage(self.driver)
        page.go_to_page_url()

        # Select from dropdown row which will meet all criteria



        # 1.	Item contains „Exercise”
        # 2.	Units contains  Ea
        # 3.	Unit Cost greater than 1.1

        # TODO delete, only for observation purposes
        time.sleep(2.0)
