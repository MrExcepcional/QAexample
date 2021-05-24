import os
import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
URL = "https://staging.scrive.com/t/9221714692410699950/7348c782641060a9"
MAX_WAIT = 10

class FunctionalTest(unittest.TestCase):


    def setUp(self):
        self.browser = self.get_browser("Firefox")
        if not self.browser:
            raise Exception("No valid browser name detected.")
        self.staging_server = URL

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{browser}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            browser=self.browser.name,
            timestamp=timestamp
        )

    def take_screenshot(self):
        if not os.path.exists(SCREEN_DUMP_LOCATION):
            os.makedirs(SCREEN_DUMP_LOCATION)
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.browser.get_screenshot_as_file(filename)

    def get_browser(self, browser_name):
        if browser_name.lower() == "firefox":
            return webdriver.Firefox()
        elif browser_name.lower() == "chrome":
            return webdriver.Chrome()
        else:
            return None

    def ***REMOVED***(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

    @***REMOVED***
    def ***REMOVED***_for_next_button_to_turn_active(self):
        next_button = self.browser.find_element_by_css_selector(
            'a[data-reactid=".0.4.9.0.0"]'
            )
        self.assertIn("Next", next_button.text)
        return next_button

    @***REMOVED***
    def ***REMOVED***_for_confirmation_modal(self, confirmation_text):
        modal = self.browser.find_element_by_css_selector(
            'div[data-reactid=".0.4.9"]'
            )
        self.assertIn(confirmation_text, modal.text)

    @***REMOVED***
    def ***REMOVED***_for_documet_signed_confirmation(self):
        confirmation = self.browser.find_element_by_css_selector(
            'span[data-reactid=".0.4.2.1.0.0.0.0"]'
            )
        self.assertIn("Document signed!", confirmation.text)