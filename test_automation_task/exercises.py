import time
import unittest

from hamcrest import assert_that
from selenium import webdriver
from selenium.webdriver import ActionChains

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

        # page.set_age_slider_to(40)

        slider_track_locator = (By.XPATH, "//*[@class='hSliderTrack']")
        slider_thumb_locator = (By.XPATH, "//*[@class='hSliderThumb']")
        slider_range_values = (By.XPATH, "//*[@class='sliderRange']/div")

        assert_that(self, waits_to_have(ec.visibility_of_element_located, slider_track_locator))
        slider_track = self.driver.find_element(*slider_track_locator)
        width_of_slider_track = slider_track.size["width"]

        assert_that(self, waits_to_have(ec.element_to_be_clickable, slider_thumb_locator))
        slider_thumb = self.driver.find_element(*slider_thumb_locator)
        width_of_slider_thumb = slider_thumb.size["width"]

        slider_range_elements = self.driver.find_elements(*slider_range_values)
        max_life_span = max([int(element.text) for element in slider_range_elements])

        movement_space_of_thumb = width_of_slider_track - width_of_slider_thumb
        get_position_on_slider = lambda age : int(movement_space_of_thumb * age / max_life_span)
        x_offset = get_position_on_slider(40) - movement_space_of_thumb

        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider_thumb, x_offset, 0)
        actions.perform()


        # 3.	Sort order by „Life Span”
        # 4.	Select checkbox  to Ascending
        #
        # Assert that results contains more than 12 items

        # TODO delete, only for observation purposes
        time.sleep(2.0)
