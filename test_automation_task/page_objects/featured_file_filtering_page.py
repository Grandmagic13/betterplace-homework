from test_automation_task.page_objects.smart_client_page import SmartClientPage


class FeaturedFileFilteringPage(SmartClientPage):

    def __init__(self, driver):
        super(FeaturedFileFilteringPage, self).__init__(driver)
        self.base_page = self.__create_subpage_url()

    def __create_subpage_url(self):
        return "{0}/{1}".format(self.base_page, "#featured_tile_filtering")
