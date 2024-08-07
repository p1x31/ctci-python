class Solution:
    def countBits(self, n: int) -> List[int]:
        #integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
        #156 ms
        # ans = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     ans[i] = ans[i >> 1] + (i & 1)
        # return ans[:n+1]
        #81ms
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + i % 2
        return ans[:n+1]    