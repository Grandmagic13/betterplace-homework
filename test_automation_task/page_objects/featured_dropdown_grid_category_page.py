from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_automation_task.page_objects.smart_client_page import *
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
        self.base_page = create_subpage_url(self.base_page, "#featured_dropdown_grid_category")

    def select_and_return_item_based_on_criteria(self, criteria):
        self.click(self.DROPDOWN_ARROW_LOCATOR)

        scroll_thumb = self.find_clickable(self.SCROLL_TUMB_LOCATOR)
        scroll_track = self.find_element(self.SCROLL_TRACK_LOCATOR)
        scroll_space_size = scroll_track.size["height"] - scroll_thumb.size["height"]

        return self.__find_matching_item(criteria, scroll_space_size, scroll_thumb)

    def __find_matching_item(self, criteria, scroll_space_size, scroll_thumb):
        while scroll_space_size > 0:
            loaded_item_rows = self.find_elements(self.ITEM_ROWS_LOCATOR)
            matching_item = self.__find_item_meeting_criteria_in(loaded_item_rows, criteria)
            if matching_item is not None:
                matching_item.click()
                return matching_item
            self.__scroll_down_dropdown(scroll_thumb)
            scroll_space_size -= self.SCROLL_OFFSET
        return None

    def __find_item_meeting_criteria_in(self, list, criteria):
        for item in list:
            item_attributes = item.find_elements(*self.ATTRIBUTES_SUBLOCATOR)
            if not self.__are_criteria_met_for_item_attributes(item_attributes, criteria):
                continue
            print("Item: {0}, Units: {1}, Unit Cost: {2}"
                  .format(item_attributes[self.ITEM].text, item_attributes[self.UNITS].text,
                          item_attributes[self.UNIT_COST].text))
            return item
        return None

    def __scroll_down_dropdown(self, scroll_thumb):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(scroll_thumb, 0, self.SCROLL_OFFSET)
        actions.perform()

    def __are_criteria_met_for_item_attributes(self, item_attributes, criteria):
        for attribute, is_criteria_met in criteria.items():
            if not is_criteria_met(item_attributes[attribute].text):
                return False
        return True
