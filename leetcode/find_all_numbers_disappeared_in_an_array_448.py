from collections import Counter
def findDisappearedNumbers(nums):
        #nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#         counter = Counter(nums)
#         print(counter)
#         return [i for i in range(1, len(nums) + 1) if i not in counter]
# print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
# print(findDisappearedNumbers([1,1]))

        #526 ms
        #counter = Counter(nums)
        #return [i for i in range(1, len(nums) + 1) if i not in counter]
        #358 ms
        set_nums = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in set_nums]
        
        # cyclic sort 680 ms
        # i = 0
        # while i < len(nums):
        #     pos = nums[i] - 1 # correct position
        #     if nums[i] != nums[pos]:
        #         nums[i], nums[pos] = nums[pos], nums[i]
        #     else:
        #         i += 1
        
        # miss = []
        
        # for i in range(len(nums)):
        #     if nums[i] != i + 1:
        #         miss.append(i + 1)
                
        # return miss