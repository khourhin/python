#! /usr/bin/python3
import re

roman_numeral_pattern = re.compile('''
^
M{0,4}
(CM|CD|D?C{0,3})
(XC|XL|L?X{0,3})
(IX|IV|V?I{0,3})
$
''', re.VERBOSE
)


roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

# Defining new exception class to catch it in the test
class OutOfRangeError(ValueError): pass

class NotIntegerError(ValueError): pass

class InvalidRomanNumeralError(ValueError): pass

def to_roman(number):
    '''
    Convert integer to roman numeral
    '''
    result = ''

    if not isinstance(number, int):
        raise NotIntegerError('not an integer')

    if not (0 < number < 5000):
        raise OutOfRangeError('number out of range (should be <5000)')

    
    for numeral, integer in roman_numeral_map:
        while number >= integer:
            result += numeral
            number -= integer

    return result
    

def from_roman(s):
    '''
    Convert roman numeral to integer
    '''

    if not s:
        raise InvalidRomanNumeralError('Input cannot be blank')
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    
    result = 0
    index = 0

    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index +=len(numeral)
    
    return result

    

