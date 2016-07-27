#! /usr/bin/python3
import roman2
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (4000, 'MMMM'),
                     (4500, 'MMMMD'),
                     (4888, 'MMMMDCCCLXXXVIII'),
                     (4999, 'MMMMCMXCIX') )

    def test_to_roman_known_values(self):
        ''' 
        to_roman should give known result with known input 
        '''

        for integer, numeral in self.known_values:
            result = roman2.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''
        from_roman should give known result with known input         
        '''

        for integer, numeral in self.known_values:
            result = roman2.from_roman(numeral)
            self.assertEqual(integer, result)

class RoundTripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''
        from_roman(to_roman(n)) == n for all n
        '''
        for integer in range(1,5000):
            numeral = roman2.to_roman(integer)
            result = roman2.from_roman(numeral)
            self.assertEqual(integer, result)
        
class ToRomanBadInput(unittest.TestCase):
    def test_not_integer(self):
        '''
        shoudl only accept integers
        '''
        self.assertRaises(roman2.NotIntegerError, roman2.to_roman, "A")
        self.assertRaises(roman2.NotIntegerError, roman2.to_roman, 0.1)
        
    def test_too_large(self):
        '''
        to roman shoud fail with large input
        '''
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 5000)

    def test_zero(self):
        '''
        to_roman should fail with 0
        '''
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 0)
        
    def test_negative(self):
        '''
        to_roman should fail with 0
        '''
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, -1)

class FromRomanBadInput(unittest.TestCase):
    def test_blank(self):
        '''
        from_roman should fail if empty strin is given
        '''
        self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, '')
        
    def test_too_many_repeated_numerals(self):
        '''
        from_roman should fail with too many repeated numerals
        '''
        for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)

    def test_repeated_pairs(self):
        '''
        from_roman should fail with repeated pairs of numerals
        '''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)

    def test_malformed_antecedents(self):
        '''
        from_roman should fail with malformed antecedents
        '''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman2.InvalidRomanNumeralError, roman2.from_roman, s)
        
if __name__ == "__main__":
    unittest.main()
    
