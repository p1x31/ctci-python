from typing import (
    List,
)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #only can contain k 0's
        slow = 0
        max_count = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                k -= 1
            # when k become negative, we need to move slow pointer
            while k < 0:
                #shrink window
                if nums[slow] == 0:
                    k += 1
                slow += 1
            if fast - slow + 1 > max_count:
                max_count = fast - slow + 1
        return max_count

l = Solution()
print(l.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))
l.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 2)