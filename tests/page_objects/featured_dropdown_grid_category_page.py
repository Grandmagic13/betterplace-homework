from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.page_objects.smart_client_page import *
from selenium.webdriver.support import expected_conditions as ec


class FeaturedDropdownGridCategoryPage(SmartClientPage):
    ITEM = 0
    UNITS = 1
    UNIT_COST = 2
    DROPDOWN_ARROW_LOCATOR = (By.XPATH, generate_combo_box_xpath("Item"))
    ITEM_ROWS_LOCATOR = (By.XPATH, "//tr[contains(@id, 'isc_PickListMenu_0_row_')]")
    SCROLL_TUMB_LOCATOR = (By.XPATH, "//label[text()='Item']/following::div[@class='vScrollThumb']")
    SCROLL_TRACK_LOCATOR = (By.XPATH, "//label[text()='Item']/following::img[@class='vScrollTrack']")
    ATTRIBUTES_SUBLOCATOR = (By.XPATH, "td/div")
    SCROLL_OFFSET = 3

    def __init__(self, driver):
        super(FeaturedDropdownGridCategoryPage, self).__init__(driver)
        self.url = create_subpage_url(self.url, "#featured_dropdown_grid_category")

    def select_and_return_item_based_on_criteria(self, criteria):
        self.click(self.DROPDOWN_ARROW_LOCATOR)

        scroll_thumb = self.find_clickable(self.SCROLL_TUMB_LOCATOR)
        scroll_track = self.find_element(self.SCROLL_TRACK_LOCATOR)
        scroll_space_size = scroll_track.size["height"] - scroll_thumb.size["height"]

        while scroll_space_size > 0:
            matching_item = self.__find_item_meeting_criteria(criteria)
            if matching_item is not None:
                matching_item.click()
                return matching_item
            self.__scroll_down_dropdown(scroll_thumb)
            scroll_space_size -= self.SCROLL_OFFSET
        return None

    def __find_item_meeting_criteria(self, criteria):
        loaded_item_rows = self.find_elements(self.ITEM_ROWS_LOCATOR)
        for item in loaded_item_rows:
            item_attributes = item.find_elements(*self.ATTRIBUTES_SUBLOCATOR)
            if not self.__are_criteria_met_for_item_attributes(item_attributes, criteria):
                continue
            return item
        return None

    def __scroll_down_dropdown(self, scroll_thumb):
        self.scroll_down_dropdown(scroll_thumb, self.SCROLL_OFFSET)

    def __are_criteria_met_for_item_attributes(self, item_attributes, criteria):
        for attribute, is_criteria_met in criteria.items():
            if not is_criteria_met(item_attributes[attribute].text):
                return False
        return True
