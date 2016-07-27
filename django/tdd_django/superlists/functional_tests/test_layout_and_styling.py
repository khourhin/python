#! /usr/bin/python3

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Buck goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        # He sees that the input box is centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            512,
            delta=5
        )

        # He starts a new list and sees the input is centered to
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
        
