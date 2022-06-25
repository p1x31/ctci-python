from collections import OrderedDict
def roman_to_int(str):
    """
    Convert a Roman numeral to an integer.
    """
    roman_numerals = OrderedDict([
        (900, 'CM'),
        (400, 'CD'),
        (90, 'XC'),
        (40, 'XL'),
        (9, 'IX'),
        (4, 'IV'),
        (50, 'L'),
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ])

    out = 0
    for value, letter in roman_numerals.items():
        out += value * str.count(letter)
        str = str.replace(letter, '')
    return out

roman_to_int("VIII")