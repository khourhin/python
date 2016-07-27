#! /usr/bin/python3

from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
    
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can not have an empty list item')
    
        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Rule the world')
        self.check_for_row_in_list_table('1: blabla')
    
        # Perversely, she now decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # She receives a similar warning on the list page_text
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can not have an empty list item')
        
        # And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('build time machine')
        self.check_for_row_in_list_table('1: Rule the world')
        self.check_for_row_in_list_table('2: build time machine')
