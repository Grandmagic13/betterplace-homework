class SmartClientPage:

    def __init__(self, driver):
        self.base_page = "http://www.smartclient.com/smartgwt/showcase"
        self.driver = driver

    def go_to_page_url(self):
        self.driver.get(self.base_page)
