class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # complements = {} #key: compliment, value: index hashmap
        # result = []
        # target = 0
        # if len(nums) < 3:
        #     return result
        # else:
        #     complements[nums[0]] = 0
        #     for index, item in enumerate(nums):
        #         if complements.get(item) is None:
        #             # we are looking for difference between target and given number
        #             #put index at the target-item position
        #             complements[target - nums[0] - item] = (index+1)
        #         else:
        #             # replace 0 with k use pointer to iterate through smth like this MAYBE set first number as target
        #             result = [nums[0], complements.get(item), list(complements.values()).index(index)]
        # return result
        #1432 ms
        # res = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     l, r = i+1, len(nums)-1
        #     while l < r:
        #         s = nums[i] + nums[l] + nums[r]
        #         if s < 0:
        #             l += 1
        #         elif s > 0:
        #             r -= 1
        #         else:
        #             res.append([nums[i], nums[l], nums[r]])
        #             while l < r and nums[l] == nums[l+1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r-1]:
        #                 r -= 1
        #             l += 1
        #             r -= 1
        # return res
        #1288 ms
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            # i > 0 not the first value in the array and a is the same as the previous value
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                #t0o small
                if three_sum < 0:
                    l += 1
                #too big
                elif three_sum > 0:
                    r -= 1
                #if equal to 0
                else:
                    res.append([a, nums[l], nums[r]])
                    #skip duplicates dont wanna have the same sum
                    l += 1
                    #dont need to update right pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1    
        return res