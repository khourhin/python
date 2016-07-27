#! /usr/bin/python3

import re
import itertools

# RE
def playing_with_re():

    # Phone number
    # Using verbose re patterns
    
    numbers = ["000-112-1541", "my phone: 000-154-7887", "       000-156-1564x1234"]
    
    pat = """
    (\d{3}) # 3 digits
    -
    (\d{3}) # 3 digits
    -
    (\d{4})x?(\d*) # 4 digits and extension separated by "x"
    """
    
    # Don't forget the last argument re.VERBOSE to use the verbose syntax for re
    print([ re.search(pat, x, re.VERBOSE).groups() for x in numbers ])

#-------------------------------------------------------------------------------
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """
    Convert a file size in human readable
    """
    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

    if size < 0:
        raise ValueError("Size cannot be negative")

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('Number to large')

#-------------------------------------------------------------------------------
def solve(puzzle):
    # Example ./exercises.py "I + LOVE + YOU == DORA"
    
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
                        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation
    

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    
#    print(approximate_size(int(sys.argv[1])))
    
for puzzle in sys.argv[1:]:
    print(puzzle)
    solution = solve(puzzle)
    if solution:
        print(solution)
