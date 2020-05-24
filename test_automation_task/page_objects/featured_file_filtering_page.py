from selenium.webdriver.common.by import By

from test_automation_task.page_objects.smart_client_page import SmartClientPage


class FeaturedFileFilteringPage(SmartClientPage):

    ANIMAL_TEXT_INPUT_LOCATOR = (By.XPATH, "//label[text()='Animal']/following::input")

    def __init__(self, driver):
        super(FeaturedFileFilteringPage, self).__init__(driver)
        self.base_page = self.__create_subpage_url()

    def __create_subpage_url(self):
        return "{0}/{1}".format(self.base_page, "#featured_tile_filtering")

    def send_keys_to_animal_input(self, keys):
        self.send_keys_to_element(self.ANIMAL_TEXT_INPUT_LOCATOR, keys)
