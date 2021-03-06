#! /usr/bin/python3

from selenium import webdriver
import unittest

class VisitTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8001')

        self.assertIn('To-Do', self.browser.title)
        self.fail('More to do here')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
