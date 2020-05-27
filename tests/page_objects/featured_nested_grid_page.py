import random
import string
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.page_objects.smart_client_page import *
from selenium.webdriver.support import expected_conditions as ec


class FeaturedNestedGridPage(SmartClientPage):
    # ARROW_1_LOCATOR = (By.XPATH, "//div[text()='Item']/following::tr[@role='listitem' and @aria-posinset='1']//span")
    FOLLOWING_ITEM_XPATH = "//div[text()='Item']/following::"
    FOLLOWING_DESCRIPTION_XPATH = "//div[text()='Description']/following::"
    ITEM_BY_INDEX_XPATH = FOLLOWING_ITEM_XPATH + "tr[@role='listitem' and @aria-posinset='{index}']"
    NESTED_ITEM_BY_INDEX_XPATH = FOLLOWING_DESCRIPTION_XPATH + "tr[@role='listitem' and @aria-posinset='{index}']"
    NESTED_ITEM_DESCRIPTION_BY_INDEX_XPATH = NESTED_ITEM_BY_INDEX_XPATH + "//td[3]/div"
    ARROW_BY_INDEX_XPATH = ITEM_BY_INDEX_XPATH + "//span"
    PARENT_BUTTON_XPATH = "/parent::td[@class='button']"
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Save']" + PARENT_BUTTON_XPATH)
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Close']" + PARENT_BUTTON_XPATH)
    TEXTAREA_LOCATOR = (By.XPATH, "//textarea")

    def __init__(self, driver):
        super(FeaturedNestedGridPage, self).__init__(driver)
        self.url = create_subpage_url(self.url, "#featured_nested_grid")

    def change_sub_items_for_items_with_name_containing_correction(self):
        # check if row / item needs to be modified

        # if needs to be modified
        # change 1 item without conditions
        arrow_1_locator = self.arrow_locator_by_index(1)
        self.click(arrow_1_locator)
        nested_index = 1
        while self.description_by_index_exists(nested_index):
            description_locator = self.description_locator_by_index(nested_index)
            self.move_to_element(description_locator)
            self.click(description_locator)
            new_description = "{index} {random_string}".format(index=nested_index, random_string=self.get_random_10_long_string())
            self.send_keys_to_element(self.TEXTAREA_LOCATOR, new_description)
            self.click(self.SAVE_BUTTON_LOCATOR)
            nested_index += 1

        self.click(self.CLOSE_BUTTON_LOCATOR)

    def description_by_index_exists(self, index):
        return len(self.find_elements(self.description_locator_by_index(index))) > 0

    def move_to_element(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def arrow_locator_by_index(self, index):
        return By.XPATH, self.ARROW_BY_INDEX_XPATH.format(index=index)


    def description_locator_by_index(self, index):
        return By.XPATH, self.NESTED_ITEM_DESCRIPTION_BY_INDEX_XPATH.format(index=index)

    def get_random_10_long_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
