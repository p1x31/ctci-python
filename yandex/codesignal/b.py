def find_substrings(pattern, source):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0
    for i in range(len(source) - len(pattern) + 1):
        if len(pattern) != len(source[i:i+len(pattern)]):
            continue
        for j in range(len(pattern)):
            if pattern[j] == '0' and source[i+j] not in vowels:
                break
            elif pattern[j] == '1' and source[i+j] not in consonants:
                break
        else:
            count += 1
    return count