def pivotIndex(nums) -> int:
    # pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    #If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    #If the index is on the right edge of the array, then the right sum is 0 because there are no elements to the right.
    # compare the left and right sums
    # if any(sum(nums[key+1:]) == sum(nums[0:key-1]) for key, value in enumerate(nums)):
    #     return True
    # else:
    #     return -1
    #sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
    
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2, 1 , -1]))