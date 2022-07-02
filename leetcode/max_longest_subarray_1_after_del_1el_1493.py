from typing import (
    List,
)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #you should delete one element from it.
        #Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
        slow = 0
        max_count = 0
        k = 1
        for fast, value in enumerate(nums):
            if value == 0:
                k -= 1
            # when k become negative, we need to move slow pointer
            while k < 0:
                #shrink window
                if nums[slow] == 0:
                    k += 1
                slow += 1
            #dont add one as we deleting the element
            if fast - slow > max_count:
                max_count = fast - slow
        return max_count