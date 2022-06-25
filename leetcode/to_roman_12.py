from collections import OrderedDict

def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.
    """
    roman_numerals = OrderedDict([
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ])

    roman_numeral = ''
    for value, letter in roman_numerals.items():
        while num >= value:
            roman_numeral += letter
            num -= value
    return roman_numeral