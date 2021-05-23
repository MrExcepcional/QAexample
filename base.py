import os
import unittest
from datetime import datetime

from selenium import webdriver

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
URL = "https://staging.scrive.com/t/9221714692410699950/7348c782641060a9"

class FunctionalTest(unittest.TestCase):


    def setUp(self):
        self.browser = get_browser("Firefox")
        if not self.browser:
            raise Exception("No valid browser name detected.")
        self.staging_server = URL

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{browser}-window{windowid}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            browser=self.browser.name,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def take_screenshot(self):
        if not os.path.exists(SCREEN_DUMP_LOCATION):
            os.makdirs(SCREEN_DUMP_LOCATION)
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