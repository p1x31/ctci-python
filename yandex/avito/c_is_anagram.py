from sys import stdin

S = lambda: stdin.readline().strip().split()

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    
    for i, value in enumerate(s):
        count_s[value] = 1 + count_s.get(value, 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    return True

def main():
    string_s, string_t = S()
    print(str(is_anagram(string_s, string_t)).lower())
if __name__ == "__main__":
    main()