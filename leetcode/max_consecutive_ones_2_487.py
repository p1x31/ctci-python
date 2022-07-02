from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        #  if you can flip at most one 0.
        slow = 0
        max_count = 0
        k = 1
        for fast, value in enumerate(nums):
            if value == 0:
                k -= 1
            # when k become negative, we need to move slow pointer
            while k < 0:
                if nums[slow] == 0:
                    k += 1
                slow += 1
            if fast - slow + 1 > max_count:
                max_count = fast - slow + 1
        return max_count