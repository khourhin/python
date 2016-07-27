#! /usr/bin/python3

import unittest
import reader

class ReaderTest(unittest.TestCase):
    test_f = "pubmed.xml"

    def test_find_correct_number_of_items(self):
        self.assertEqual(len(reader.getitem(self.test_f, "item")), 15 )
        
if __name__ == "__main__":
    unittest.main()
    
