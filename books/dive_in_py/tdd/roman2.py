#! /usr/bin/python3

to_roman_table = [None]
from_roman_table = {}

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

    if not isinstance(number, int):
        raise NotIntegerError('not an integer')

    if not (0 < number < 5000):
        raise OutOfRangeError('number out of range (should be <5000)')

    return to_roman_table[number]
    
def from_roman(s):
    '''
    Convert roman numeral to integer
    '''

    if not isinstance(s, str):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    if not s:
        raise InvalidRomanNumeralError('Input cannot be blank')
    if s not in from_roman_table:
        raise InvalidRomanNumeralError('Input cannot be blank')
    
    return from_roman_table[s]

def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:2
            result += to_roman_table[n]
        return result

    for integer in range(1,5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer
            
build_lookup_tables()
