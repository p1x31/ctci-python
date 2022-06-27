from collections import Counter
def singleNumber(nums):
    #nums, every element appears twice except for one. Find that single one.
    #nums = [1,1,2,3,3]
#     counter = Counter(nums)
#     n = len(set(nums))
#     #n - 1 last element of most common tuples; [0] FIRST element of the tuple (the number) not the count
#     print(counter.most_common()[n-1])
#     return counter.most_common()[n-1][0]
# print(singleNumber([1,1,2,3,3]))

# print(singleNumber([4,1,2,1,2]))
    #238 ms
    mask = 0

    for num in nums:
        mask ^= num
    return mask

print(singleNumber([1,1,2,3,3]))

print(singleNumber([4,1,2,1,2]))