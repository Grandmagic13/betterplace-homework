from selenium.webdriver.common.by import By

from tests.page_objects.page import Page


class AmazonPage(Page):
    SEARCHBOX_LOCATOR = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//input[@class='nav-input' and @value='Go']")
    RESULT_LOCATOR = (By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[contains(@class, 's-result-item') and @data-index > 0]")

    def __init__(self, driver):
        super(AmazonPage, self).__init__(driver, url="https://www.amazon.com/")

    def search_for_item(self, item):
        self.send_keys_to_element(self.SEARCHBOX_LOCATOR, item)
        self.click(self.SEARCH_BUTTON)

    def get_number_of_hits(self):
        return len(self.find_elements(self.RESULT_LOCATOR))

    def measure_response_time_in_milliseconds_and_get_number_of_hits(self):
        response_time = self.measure_response_time_in_milliseconds()
        number_of_hits = self.get_number_of_hits()
        return {
            "response time" : response_time,
            "number of hits" : number_of_hits
        }

    def measure_response_time_in_milliseconds(self):
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        return domComplete - responseStart