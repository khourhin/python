#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # tell selenium to wait for the results up to 3 seconds
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Buck want to use an online to-do app.
        # He goes check this homepage:
        self.browser.get('http://localhost:8000')
        
        # The page title and header mention "to do"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        # He type "Buy milk"

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy milk" as an item in a to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')                
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy milk')
        
        # There is still a text box inviting him to add another item. He
        # enters "Buy cereals"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy cereals')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Buy cereals')

        # Buck wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        self.fail("Still more to do ...")

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')
            
