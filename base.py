import os
import unittest
from datetime import datetime

from selenium import webdriver

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
URL = "https://staging.scrive.com/t/9221714692410699950/7348c782641060a9"

browsers = ["Firefox", "Chrome"]

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
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
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.browser.get_screenshot_as_file(filename)
