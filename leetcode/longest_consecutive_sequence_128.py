from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #468 ms 
        # num_set = set(nums)
        # longest = 0
        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_longest = 1
        #         while num + 1 in num_set:
        #             num += 1
        #             current_longest += 1
        #         longest = max(longest, current_longest)
        # return longest
        #513 ms
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest