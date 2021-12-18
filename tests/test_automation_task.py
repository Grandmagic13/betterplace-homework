import unittest

from hamcrest import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.custom_matchers.wait_for_matcher import waits_to_have
from tests.page_objects.charity_page import CharityPage
from selenium.webdriver.support import expected_conditions as ec


class BetterPlaceTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        mobile_emulation = {
            "deviceMetrics": {"width": 380, "height": 800, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 11; Pixel 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def test_submit_donation(self):
        page = CharityPage(self.driver)
        page.go_to_page_url()
        page.close_cookie_banner()
        page.enter_donation_amount("5", override=True)
        page.choose_direct_deposit_payment_method()

        # check payment method collision

        page.fill_form()
        page.submit()
        assert_that(page, waits_to_have(ec.title_contains, CharityPage.RECEIPT_TITLE_LOCATOR))

        # TODO modify dev notes
        # TODO add dev note about how this might have been solved more elegantly with jquery?