class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return true if x is palindrome integer.
        if x < 0:
            return False
        if x - int(str(x)[::-1]) == 0:
            return True
        return False