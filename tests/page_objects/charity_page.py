from selenium.webdriver.common.by import By

from tests.page_objects.page import Page


class CharityPage(Page):

    COOKIES_OKAY_BUTTON_LOCATOR = (By.XPATH, "//div[@class='cookie-content-wrapper']//button[text()='Okay!']")
    DONATION_INPUT_LOCATOR = (By.XPATH, "//div[@class='donations-form-amount-selection']//input[@name='amount_cents']")
    DIRECT_DEPOSIT_RADIOBUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'payment-method-radios')]//span[text()='Überweisung']/preceding-sibling::span")
    FORM_FIRST_NAME = (By.XPATH, "//input[@id='first_name']")
    FORM_LAST_NAME = (By.XPATH, "//input[@id='last_name']")
    FORM_EMAIL = (By.XPATH, "//input[@id='email']")

    def __init__(self, driver, toggle_bugged_page=False):
        postfix = "?force-bug=1" if toggle_bugged_page else ""
        super(CharityPage, self).__init__(driver, url="https://www.bp42.com/de/donate/platform/projects/1114{}".format(postfix))

    def close_cookie_banner(self):
        self.click(self.COOKIES_OKAY_BUTTON_LOCATOR)

    def enter_donation_amount(self, text_amount, override=False):
        self.send_keys_to_element(self.DONATION_INPUT_LOCATOR, text_amount, override)

    def choose_direct_deposit_payment_method(self):
        self.click(self.DIRECT_DEPOSIT_RADIOBUTTON_LOCATOR)

    def fill_form(self):
        self.send_keys_to_element(self.FORM_FIRST_NAME, "TestFirstName")
        self.send_keys_to_element(self.FORM_LAST_NAME, "TestLastName")
        self.send_keys_to_element(self.FORM_EMAIL, "testbot@betterplace.org")


