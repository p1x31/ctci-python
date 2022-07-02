from calendar import c


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        #maximum number of consecutive 1's in the array.
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
        return max_count
        #dp 534ms
        # consecutive = result = 0
        # for n in nums:
        #     consecutive = consecutive*n+n
        #     result = max(result, consecutive)
        # return result
