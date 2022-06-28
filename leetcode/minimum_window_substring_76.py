from itertools import count


class Solution:
    def minWindow(self, s: str, t: str) -> str:
    # minimum window substring of s such that every character in t (including duplicates) is included in the window. 
    # If there is no such window in s that covers all characters in t, return the empty string "".
    # Example 1:
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    # Example 2:
    # Input: s = "a", t = "aa"
    # Output: ""
    # Note:
    # If there are multiple valid solutions, return any of them.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                #remove the leftmost character
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""