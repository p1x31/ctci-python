class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        #three integers in nums such that the sum is closest to target
        res = sum(nums[0:3])
        nums.sort()
        if len(nums) == 3:
            return sum(nums)
        for i, a in enumerate(nums):
            # i > 0 not the first value in the array and a is the same as the previous value
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                #t0o small
                if three_sum == target:
                    return target
                #It is to update the distance of final sum (res) with the current sum(sum)
                # example: consider [-4,-1,1,2] as the initial sorted array
                # res = sum(nums[:3]) = -4+(-1)+(1) = -4
                # now, s is suppose sum of -1,2,1 = 2
                # target = 1
                # abs(s-target) < abs(res-target) :
                # abs(2-1) < abs(-4-1)
                # res = 2
                # basically updating the closest sum.
                if abs(three_sum-target) < abs(res - target):
                    res = three_sum
                if three_sum < target:
                    l += 1
                #too big
                else:
                    r -= 1       
        return res

        #308 ms
        # def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # return self.KSumClosest(nums, 3, target)

        # def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        #     N = len(nums)
        #     if N == k:
        #         return sum(nums[:k])

        #     current = sum(nums[:k])
        #     if current >= target:
        #         return current

        #     current = sum(nums[-k:])
        #     if current <= target:
        #         return current
            
        #     if k == 1:
        #         return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        #     closest = sum(nums[:k])
        #     for i, x in enumerate(nums[:-k+1]):
        #         if i>0 and x == nums[i-1]:
        #             continue
        #         current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
        #         if abs(target - current) < abs(target - closest):
        #             if current == target:
        #                 return target
        #             else:
        #                 closest = current

        #     return closest