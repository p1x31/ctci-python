class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        # create a dictionary of characters and their counts
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return sum(char_counts.values() if char_counts[char] % 2 == 0 else char_counts.values() - 1 for char in char_counts)