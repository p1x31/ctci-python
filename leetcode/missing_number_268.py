def missingNumber(nums) -> int:
    # array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
print(missingNumber([9,6,4,2,3,5,7,0,1]))