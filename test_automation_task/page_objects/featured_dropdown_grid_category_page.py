from test_automation_task.page_objects.smart_client_page import *


class FeaturedDropdownGridCategoryPage(SmartClientPage):
    def __init__(self, driver):
        super(FeaturedDropdownGridCategoryPage, self).__init__(driver)
        self.base_page = create_subpage_url(self.base_page, "#featured_dropdown_grid_category")