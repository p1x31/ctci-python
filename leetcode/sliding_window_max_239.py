import collections
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        output = []
        q = collections.deque() # queue of indices
        l = r = 0
        while r < len(nums):
            #compare with the last element in the array nums vs last elemnt in the window = last queue element
            while q and nums[q[-1]] < nums[r]:
                 #pop from the rightmost position
                q.pop()
            q.append(r)
            # remove the leftmost index if it is out of range
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

#example [8, 7, 6, 9]
# deque [8, 7, 6, 9] [8, 7] before we add anything pop line 13 [7]
# 6 > 7 is not so  put 6 in [7, 6] last put to output line 17 
# 9 > 7  pop 7 first than put 9 in [9] line 13