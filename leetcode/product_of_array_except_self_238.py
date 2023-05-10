from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #431 ms
        # res = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     res[i] = res[i - 1] * nums[i - 1]
        # right = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] = res[i] * right
        # already stored prefix product
        #     right *= nums[i]
        # return res
        #300ms
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # what next line do is to iterate through the list in reverse order last -1 means
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
