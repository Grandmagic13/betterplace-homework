from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_automation_task.page_objects.smart_client_page import SmartClientPage


class FeaturedFileFilteringPage(SmartClientPage):
    SORT_ORDER_OPTION_LIFE_SPAN = "Life Span"

    ANIMAL_TEXT_INPUT_LOCATOR = (By.XPATH, "//label[text()='Animal']/following::input")
    MAX_LIFE_SPAN_TRACK_LOCATOR = (By.XPATH, "//*[@class='hSliderTrack']")
    MAX_LIFE_SPAN_THUMB_LOCATOR = (By.XPATH, "//*[@class='hSliderThumb']")
    MAX_LIFE_SPAN_SLIDER_RANGE_VALUES = (By.XPATH, "//*[@class='sliderRange']/div")
    SORT_ORDER_LOCATOR = (By.XPATH, "//label[text()='Sort by']/following::span[@class='comboBoxItemPicker']")
    ASCENDING_CHECKBOX_LOCATOR = (By.XPATH, "//label[text()='Ascending']/preceding-sibling::span")

    def __init__(self, driver):
        super(FeaturedFileFilteringPage, self).__init__(driver)
        self.base_page = self.__create_subpage_url()

    def __create_subpage_url(self):
        return "{0}/{1}".format(self.base_page, "#featured_tile_filtering")

    def tick_ascending_checkbox(self):
        self.click(self.ASCENDING_CHECKBOX_LOCATOR)

    def select_sort_order(self, option):
        option_locator = (By.XPATH, "//div[text()='{0}']".format(option))
        self.click(self.SORT_ORDER_LOCATOR)
        self.click(option_locator)

    def send_keys_to_animal_input(self, keys):
        self.send_keys_to_element(self.ANIMAL_TEXT_INPUT_LOCATOR, keys)

    def set_age_slider_to(self, age):
        actions = ActionChains(self.driver)
        slider_thumb = self.find_clickable(self.MAX_LIFE_SPAN_THUMB_LOCATOR)
        x_offset = self.calculate_x_offset_by_age(age)
        actions.drag_and_drop_by_offset(slider_thumb, x_offset, 0)
        actions.perform()

    def calculate_x_offset_by_age(self, age):
        max_life_span = self.__get_max_life_span()
        movement_space_of_thumb = self.__calculate_movement_space_of_slider_thumb()
        position_on_slider_for_age = int(movement_space_of_thumb * age / max_life_span)
        return position_on_slider_for_age - movement_space_of_thumb

    def __calculate_movement_space_of_slider_thumb(self):
        width_of_slider_track = self.__get_width_of(self.MAX_LIFE_SPAN_TRACK_LOCATOR)
        width_of_slider_thumb = self.__get_width_of(self.MAX_LIFE_SPAN_THUMB_LOCATOR)
        return width_of_slider_track - width_of_slider_thumb

    def __get_width_of(self, locator):
        element = self.find_element(locator)
        return element.size["width"]

    def __get_max_life_span(self):
        slider_range_elements = self.find_elements(self.MAX_LIFE_SPAN_SLIDER_RANGE_VALUES)
        return max([int(element.text) for element in slider_range_elements])
