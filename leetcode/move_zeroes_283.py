class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        #перемещаем все 0's в конец массива и оставляем порядок ненулевых элементов
        #	1841 ms
        # for k, v in enumerate(nums):
        #     if v == 0:
        #         nums.pop(nums.index(v))
        #         nums.append(0)
        #     else:
        #         continue
        #305 ms
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
l = Solution()
l.moveZeroes([0,0,1])
l.moveZeroes([0,1,0,3,12])
