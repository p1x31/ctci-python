class Solution:
    def two_sum(self,nums, target):
        compliments = {}
        result = []
        for index, item in enumerate(nums):
            if compliments.get(item) is None:
                compliments[target-item] = index
            else:
                result = [compliments[item],index]
        return result
# swap value and index check if value exists
# return index of that value and index+1 (index of the loop)

l = Solution()
print(l.two_sum([2,7,11,15],26))

#{ 24: 0, 19: 1, 15: 2}
# compliments.get(15) exists than return compliments[15]=2 and current index which is 3