first_symbol = True
result = 0
number = ''

for c in input():
    if c.isdigit():
        number += c
    elif c.isalpha() and not number:
        if first_symbol:
            first_symbol = False
        else:
            result += 1
    elif c.isalpha() and number:
        result += int(number)
        number = ''
	
if number:
    result += int(number)
else:
    result += 1
print(result)

import re

def decoded_rle_value_len(value):
    pairs = re.findall(r'(?P<letter>[A-Z])(?P<count>\d*)', value)
    return sum(int(pair[1]) if pair[1] else 1 for pair in pairs)

result = decoded_rle_value_len('A15BA5')
print(result)