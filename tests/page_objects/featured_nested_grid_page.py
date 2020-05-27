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
        # change 1 item without conditions
        arrow_1_locator = self.arrow_locator_by_index(1)
        self.click(arrow_1_locator)
        #modify elements if any
        description_1_locator = self.nested_item_description_locator_by_index(1)
        self.click(description_1_locator)
        new_description = "{index} {random_string}".format(index=1, random_string=self.get_random_10_long_string())
        self.send_keys_to_element(self.TEXTAREA_LOCATOR, new_description)
        time.sleep(2)
        #
        self.click(self.SAVE_BUTTON_LOCATOR)
        time.sleep(2)
        self.click(self.CLOSE_BUTTON_LOCATOR)

    def arrow_locator_by_index(self, index):
        return By.XPATH, self.ARROW_BY_INDEX_XPATH.format(index=index)


    def nested_item_description_locator_by_index(self, index):
        return By.XPATH, self.NESTED_ITEM_DESCRIPTION_BY_INDEX_XPATH.format(index=index)

    def get_random_10_long_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
