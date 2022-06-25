#same length, different order
from pickletools import string1


def is_one_away_same_length(string, string2):
    count_diff = 0
    for i in range(len(string)):
        if string[i] != string2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True
    
def is_one_away_diff_length(string1, string2):
    i = 0
    count_diff = 0
    while i < len(string2):
        if string1[i + count_diff] == string2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_away(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_length(s1, s2)
    else:
        return is_one_away_diff_length(s2, s1)