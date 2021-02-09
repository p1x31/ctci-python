# pointer at each index of the string
# as long as two indices are the same
class Solution(object):
    def longestPalindrome(self, s):
        largestPalindrome = ''
        for i in range(len(s)):
            palindromeOdd = self.largestPalindromeAtIndex(s, i, i)
            palindromeEven = self.largestPalindromeAtIndex(s, i, i+1)

            largerPalindrome = palindromeOdd if len(palindromeOdd) > len(palindromeEven) else palindromeEven
            # update 
            largestPalindrome = largestPalindrome if len(largestPalindrome) >= len(largerPalindrome) else largerPalindrome
        return largestPalindrome

    def largestPalindromeAtIndex(self, s, left, right):
        leftIndex = 0
        rightIndex = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftIndex = left
                rightIndex = right
            else:
                break
            left -= 1
            right += 1
        return s[leftIndex:rightIndex+1]

s = Solution()
print(s.longestPalindrome("google"))