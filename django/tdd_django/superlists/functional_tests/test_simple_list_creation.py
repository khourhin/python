#! /usr/bin/python3

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Buck want to use an online to-do app.
        # He goes check this homepage:
        self.browser.get(self.live_server_url)
        
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

        # After Buck hits enter, he is taken to a new page with his
        # todo list appearing and '1: Buy milk' as an item. 
        inputbox.send_keys(Keys.ENTER)
        buck_list_url = self.browser.current_url
        self.assertRegexpMatches(buck_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy milk')
        
        # There is still a text box inviting him to add another item. He
        # enters "Buy cereals"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy cereals')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Buy cereals')

        # A new user, Vlad, is coming. No sign of Buck list.

        ## We use a new browser to be sure that no infos are passed
        ## (through cookies for examples)
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Vlad visit the homepage, no sign of Buck data
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: Buy milk', page_text)
        self.assertNotIn('2: Buy cereals', page_text)

        # Vlad starts a new list:
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Get a beard cut')
        inputbox.send_keys(Keys.ENTER)

        # He's taken to his own url:
        vlad_list_url = self.browser.current_url
        self.assertRegexpMatches(vlad_list_url, '/lists/.+')
        self.assertNotEqual(vlad_list_url, buck_list_url)

        # And there is no trace of Buck's list still
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: Buy milk', page_text)
        self.assertIn('1: Get a beard cut', page_text)
        # other version
        self.check_for_row_in_list_table('1: Get a beard cut')
        
        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep

