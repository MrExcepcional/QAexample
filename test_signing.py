#! /usr/bin/local python3.9

import sys
import unittest

from selenium.webdriver.common.keys import Keys

from base import FunctionalTest

class SignDocumentTest(FunctionalTest):
    """docstring for SignDocumentTest"""
    
    def test_can_sign_a_document(self):
        # Daniel wants to sign a document a friend sent
        # through this cool Scrive site.
        # He goes to check out the link.
        self.browser.get(self.staging_server)

        # Daniel is aware of risk of links and make sure he
        # landed in the right site.
        # He notices the title says "Scrive".
        self.assertEqual("Scrive", self.browser.title)

        # He also notices the box inviting to fill his full name
        # with the placeholder "Your name".
        name_box = self.browser.find_element_by_id('name')
        self.assertIn("Your name", name_box.get_attribute('placeholder'))

        # Daniel enters his full name.
        name_box.send_keys('Daniel QA Leader')

        # A notorious arrow appears inviting to scroll down
        arrow = self.***REMOVED***_for_arrow_to_appear()
        # He clicks it or just scrolls down to the end of page
        arrow.click() # May be we want a separate test scrolling down?

        # He ***REMOVED***s for a "next" button to switch to active.
        button = self.***REMOVED***_for_next_button_to_turn_active()
        # He clicks next.
        button.click()

        # Now a confirmation modal appears saying
        # "...by clicking the button you will sign the document..."
        self.***REMOVED***_for_confirmation_modal("by clicking the button you will sign")
        # Now saves a screenshot
        self.take_screenshot()
        # He clicks sign
        sign_button = self.browser.find_element_by_class_name(
            "button button-block sign-button action"
            )
        sign_button.click()

        # Now a text confirms that the documet has been signed
        self.***REMOVED***_for_documet_signed_confirmation()
        # Satisfied he goes back to fika