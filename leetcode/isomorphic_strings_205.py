def isIsomorphic(s: str, t: str) -> bool:
        #determine if two strings are isomorphic
        #if they are, return True
        #if they aren't, return False
        #if they are, they must be the same length
        if len(s) != len(t):
            return False
       #if the characters in s can be replaced to get t, then they are isomorphic
        for i in range(len(s)):
            print("find s: ", s.find(s[i]), t.find(t[i]))
            if s.find(s[i]) != t.find(t[i]):
                return False
        return True
print(isIsomorphic('ab', 'aa'))
print(isIsomorphic("egg","add"))
print(isIsomorphic(s = "paper", t = "title"))
        