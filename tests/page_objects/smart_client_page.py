from selenium.webdriver import ActionChains

from tests.page_objects.page import Page


class SmartClientPage(Page):

    def __init__(self, driver):
        super(SmartClientPage, self).__init__(driver, url="http://www.smartclient.com/smartgwt/showcase")

    def scroll_down_dropdown(self, scroll_thumb, y_offset):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(scroll_thumb, 0, y_offset)
        actions.perform()


def create_subpage_url(base_page, sub_address):
    return "{0}/{1}".format(base_page, sub_address)


def generate_combo_box_xpath(label):
    return "//label[text()='{0}']/following::span[@class='comboBoxItemPicker']".format(label)
