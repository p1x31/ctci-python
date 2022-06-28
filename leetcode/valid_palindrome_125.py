class Solution:
    def isPalindrome(self, s: str) -> bool:
        #83 ms
        # new_str = ""
        # for char in s:
        #     if char.isalnum():
        #         new_str += char.lower()
        # return new_str == new_str[::-1]
        #85 ms
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #     elif not s[r].isalnum():
        #         r -= 1
        #     elif s[l].lower() != s[r].lower():
        #         return False
        #     else:
        #         l += 1
        #         r -= 1
        # return True
        # 164 ms dumbest solution
        l, r = 0, len(s) - 1
        while l < r:
            while not self.alphaNum(s[l]) and l < r:
                l += 1
            while not self.alphaNum(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self,c):
        return (ord("A") <= ord(c) <= ord("Z")) or \
            (ord("a") <= ord(c) <= ord("z")) or \
            (ord("0") <= ord(c) <= ord("9"))
l = Solution()
print(l.isPalindrome())