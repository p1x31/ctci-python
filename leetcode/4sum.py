class Solution:
    def fourSum(self, nums, target: int):
        #nums[a] + nums[b] + nums[c] + nums[d] == target
        res_list = []
        res = sum(nums[0:4])
        nums.sort()
        if len(nums) == 4:
            return sum(nums)
        for i, a in enumerate(nums):
            # i > 0 not the first value in the array and a is the same as the previous value
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                four_sum = a + nums[l] + nums[r] + nums[i+1]
                #t0o small
                if four_sum == target:
                    res_list.append([a, nums[l], nums[r], nums[i+1]])
                    return res_list
                #It is to update the distance of final sum (res) with the current sum(sum)
                # example: consider [-4,-1,1,2] as the initial sorted array
                # res = sum(nums[:3]) = -4+(-1)+(1) = -4
                # now, s is suppose sum of -1,2,1 = 2
                # target = 1
                # abs(s-target) < abs(res-target) :
                # abs(2-1) < abs(-4-1)
                # res = 2
                # basically updating the closest sum.
                elif abs(four_sum-target) < abs(res - target):
                    res = four_sum
                    res_list.append([a, nums[l], nums[r], nums[i+1]])
                if four_sum < target:
                    l += 1
                #too big
                else:
                    r -= 1
        return res_list