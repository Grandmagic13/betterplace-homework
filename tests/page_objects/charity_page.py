from hamcrest import *
from selenium.webdriver.common.by import By

from tests.page_objects.page import Page


class CharityPage(Page):

    COOKIES_OKAY_BUTTON_LOCATOR = (By.XPATH, "//div[@class='cookie-content-wrapper']//button[text()='Okay!']")
    DONATION_INPUT_LOCATOR = (By.XPATH, "//div[@class='donations-form-amount-selection']//input[@name='amount_cents']")
    DIRECT_DEPOSIT_RADIOBUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'payment-method-radios')]//span[text()='Überweisung']/preceding-sibling::span")
    FORM_FIRST_NAME_LOCATOR = (By.XPATH, "//input[@id='first_name']")
    FORM_LAST_NAME_LOCATOR = (By.XPATH, "//input[@id='last_name']")
    FORM_EMAIL_LOCATOR = (By.XPATH, "//input[@id='email']")
    SUBMIT_DONATION_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'submit-donation-button')]")
    RECEIPT_TITLE_LOCATOR = (By.XPATH, "//h1[text()='Bitte überweise deinen Spendenbetrag an unten stehende Bankverbindung']")
    PAYPAL_PAYMENT_METHOD_LABEL_LOCATOR = (By.XPATH, "//div[contains(@class, 'payment-method-radios')]/label[@for='paypal']")
    DIRECT_DEPOSIT_PAYMENT_METHOD_LABEL_LOCATOR = (By.XPATH, "//div[contains(@class, 'payment-method-radios')]/label[@for='direct_deposit']")

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
        self.send_keys_to_element(self.FORM_FIRST_NAME_LOCATOR, "TestFirstName")
        self.send_keys_to_element(self.FORM_LAST_NAME_LOCATOR, "TestLastName")
        self.send_keys_to_element(self.FORM_EMAIL_LOCATOR, "testbot@betterplace.org")

    def check_payment_method_radios_collision(self):
        # I understand there are more elegant ways to solve this, like checking collision with javascript execution
        # but I opted for a simpler solution for this specific case
        paypal_ypos = self.find_element(self.PAYPAL_PAYMENT_METHOD_LABEL_LOCATOR).location["y"]
        direct_deposit_ypos = self.find_element(self.DIRECT_DEPOSIT_PAYMENT_METHOD_LABEL_LOCATOR).location["y"]
        assert_that(direct_deposit_ypos, greater_than(paypal_ypos))

    def submit(self):
        element = self.find_clickable(self.SUBMIT_DONATION_BUTTON_LOCATOR)
        # have to scroll element into view because quicklinks banner overlaps click
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.click()


