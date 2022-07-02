from nis import match


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return true if s2 contains a permutation of s1, or false otherwise.
        #142 ms
        # if len(s1) > len(s2):
        #     return False
        # s1_count = [0] * 26
        # s2_count = [0] * 26
        # for c in s1:
        #     s1_count[ord(c) - ord('a')] += 1
        # for c in s2[:len(s1)]:
        #     s2_count[ord(c) - ord('a')] += 1
        # if s1_count == s2_count:
        #     return True
        # for i in range(len(s2) - len(s1)):
        #     s2_count[ord(s2[i]) - ord('a')] -= 1
        #     s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1
        #     if s1_count == s2_count:
        #         return True
        # return False
        #82 ms
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1
        return matches == 26
            