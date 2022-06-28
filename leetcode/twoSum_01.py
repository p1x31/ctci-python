class Solution:
    #find two values that sum to target
    #44ms
    def two_sum(self, nums, target):
        compliments = {} #key: compliment, value: index hashmap
        result = []
        for index, item in enumerate(nums):
            if compliments.get(item) is None:
                # we are looking for difference between target and given number
                #put index at the target-item position
                compliments[target-item] = index
            else:
                result = [compliments[item],index]
        return result
# swap value and index check if value exists
# return index of that value and index+1 (index of the loop)
        #122ms
        # prevMap = {} # val:index
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        # return 

l = Solution()
print(l.two_sum([2,7,11,15],26))
#26 - 2 = 24, 26 - 7 = 19, 26 - 11 = 15, 26 - 15 = 11
#{ 24: 0, 19: 1, 15: 2}
# compliments.get(15) exists than return compliments[15]=2 and current index which is 3
# 11 at intex 2, 15 at index 3