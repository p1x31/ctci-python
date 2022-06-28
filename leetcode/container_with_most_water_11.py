class Solution:
    def maxArea(self, height) -> int:
        #container with most water
        l = 0
        r = len(height) - 1
        maxleft = height[l]
        maxright = height[r]
        maxarea = 0
        # while l < r:
        #     if maxleft < maxright:
        #         maxleft = max(maxleft, height[l])
        #         maxarea = max(maxarea, (r-l)*min(maxleft, maxright))
        #         l += 1
        #     else:
        #         #(r-l) if need to cacl area of container
        #         maxright = max(maxright, height[r])
        #         maxarea = max(maxarea, (r-l)*min(maxleft, maxright))
        #         r -= 1
        # return maxarea
        while l < r:
            maxarea = max(maxarea, (r-l)*min(maxleft, maxright))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea

l = Solution()
print(l.maxArea([1,8,6,2,5,4,8,3,7]))