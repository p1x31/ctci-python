from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # result = list()
        # cur_sum = 0
        # for i, c in enumerate(nums):
        #     cur_sum += c 
        #     result.append(cur_sum)
        # return result
        return accumulate(nums)