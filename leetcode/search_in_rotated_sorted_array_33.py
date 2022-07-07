from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(N)
        # if target in nums:
        #     return nums.index(target)
        # else: 
        #     return -1
        #O(logN)
        left = 0
        right = len(nums) 
        while left < right:
            mid = (left + right) // 2
            if target < nums[0] < nums[mid]:
                left = mid + 1
            elif target >= nums[0] > nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        return -1