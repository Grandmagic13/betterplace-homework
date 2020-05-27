import random
import string

from selenium.webdriver.common.by import By

from tests.page_objects.smart_client_page import *


class FeaturedNestedGridPage(SmartClientPage):
    # ARROW_1_LOCATOR = (By.XPATH, "//div[text()='Item']/following::tr[@role='listitem' and @aria-posinset='1']//span")
    FOLLOWING_ITEM_XPATH = "//div[text()='Item']/following::"
    FOLLOWING_DESCRIPTION_XPATH = "//div[text()='Description']/following::"
    ITEM_BY_INDEX_XPATH = FOLLOWING_ITEM_XPATH + "tr[@role='listitem' and @aria-posinset='{index}']"
    ITEM_NAME_BY_INDEX_XPATH = ITEM_BY_INDEX_XPATH + "//td[2]/div"
    NESTED_ITEM_BY_INDEX_XPATH = FOLLOWING_DESCRIPTION_XPATH + "tr[@role='listitem' and @aria-posinset='{index}']"
    NESTED_ITEM_DESCRIPTION_BY_INDEX_XPATH = NESTED_ITEM_BY_INDEX_XPATH + "//td[3]/div"
    ARROW_BY_INDEX_XPATH = ITEM_BY_INDEX_XPATH + "//span"
    SCROLL_THUMB_LOCATOR = (By.XPATH, FOLLOWING_ITEM_XPATH + "div[@class='vScrollThumb']")
    PARENT_BUTTON_XPATH = "/parent::td[@class='button']"
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Save']" + PARENT_BUTTON_XPATH)
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Close']" + PARENT_BUTTON_XPATH)
    TEXTAREA_LOCATOR = (By.XPATH, "//textarea")

    SCROLL_END_LOCATOR = (By.XPATH, FOLLOWING_ITEM_XPATH + "img[@class='vScrollEnd']")
    SCROLL_TRACK_LOCATOR = (By.XPATH, FOLLOWING_ITEM_XPATH + "img[@class='vScrollTrack']")

    def __init__(self, driver):
        super(FeaturedNestedGridPage, self).__init__(driver)
        self.url = create_subpage_url(self.url, "#featured_nested_grid")
        self.driver.implicitly_wait(3)  # set implicit wait lower for slightly faster scrolling

    def change_sub_items_for_items_with_name_containing_correction(self):
        index = 1

        while self.item_by_index_exists(index):
            item_locator = self.item_locator_by_index(index)
            self.move_to_element(item_locator)

            if self.item_by_index_text_contains(index, "Correction"):
                arrow_locator = self.arrow_locator_by_index(index)
                self.click(arrow_locator)
                nested_index = 1
                while self.description_by_index_exists(nested_index):
                    description_locator = self.description_locator_by_index(nested_index)
                    self.move_to_element_and_click(description_locator)

                    new_description = "{index} {random_string}".format(index=nested_index,
                                                                       random_string=self.get_random_10_long_string())
                    self.send_keys_to_element(self.TEXTAREA_LOCATOR, new_description)
                    self.move_to_element_and_click(self.SAVE_BUTTON_LOCATOR)
                    nested_index += 1

                self.move_to_element_and_click(self.CLOSE_BUTTON_LOCATOR)
            index += 1

            if not self.item_by_index_exists(index):
                self.scroll_down_until_new_element_with_index_loads_or_reaches_end_of_bar(index)

    def scroll_down_until_new_element_with_index_loads_or_reaches_end_of_bar(self, index):
        scroll_track = self.find_element(self.SCROLL_TRACK_LOCATOR)
        scroll_thumb = self.find_clickable(self.SCROLL_THUMB_LOCATOR)
        scroll_thumb_lowest_y_position = scroll_track.location["y"] + scroll_track.size["height"] - scroll_thumb.size[
            "height"]
        while not self.item_by_index_exists(index) and self.scroll_thumb_middle_y_location(
                scroll_thumb) < scroll_thumb_lowest_y_position:
            self.scroll_down_dropdown(scroll_thumb, 20)

    def scroll_thumb_middle_y_location(self, scroll_thumb):
        return scroll_thumb.location["y"] + scroll_thumb.size["height"] / 2

    def move_to_element_and_click(self, locator):
        self.move_to_element_and_optionally_click(locator, True)

    def move_to_element(self, locator):
        self.move_to_element_and_optionally_click(locator, False)

    def move_to_element_and_optionally_click(self, locator, click):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        if click:
            actions.click()
        actions.perform()

    def item_by_index_text_contains(self, index, substring):
        return substring in self.find_element(self.item_name_locator_by_index(index)).text

    def item_name_locator_by_index(self, index):
        return By.XPATH, self.ITEM_NAME_BY_INDEX_XPATH.format(index=index)

    def item_locator_by_index(self, index):
        return By.XPATH, self.ITEM_BY_INDEX_XPATH.format(index=index)

    def arrow_locator_by_index(self, index):
        return By.XPATH, self.ARROW_BY_INDEX_XPATH.format(index=index)

    def description_by_index_exists(self, index):
        return self.element_exists(self.description_locator_by_index(index))

    def item_by_index_exists(self, index):
        return self.element_exists(self.item_locator_by_index(index))

    def element_exists(self, locator):
        return len(self.find_elements(locator)) > 0

    def description_locator_by_index(self, index):
        return By.XPATH, self.NESTED_ITEM_DESCRIPTION_BY_INDEX_XPATH.format(index=index)

    def get_random_10_long_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
