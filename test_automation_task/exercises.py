import unittest
from selenium import webdriver

# Please create scripts in programing language or tool that you know,
# Base Page:
# http://www.smartclient.com/smartgwt/showcase
from test_automation_task.page_objects.featured_file_filtering_page import FeaturedFileFilteringPage


class Exercises(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_exercise_1(self):
        # Exercise 1.
        # http://www.smartclient.com/smartgwt/showcase/#featured_tile_filtering

        page = FeaturedFileFilteringPage(self.driver)
        page.go_to_page_url()

        # Fill fields
        # 1.	Animal set using letter „a”



        # 2.	Max life span set to  40
        # 3.	Sort order by „Life Span”
        # 4.	Select checkbox  to Ascending
        #
        # Assert that results contains more than 12 items
