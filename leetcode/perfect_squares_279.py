class Solution:
    def numSquares(self, n: int) -> int:
        # TL
        # dp = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = i
        #     for j in range(1, int(i ** 0.5) + 1):
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        # return dp[n]
        #TL
        # dp = [n] * (n + 1)
        # dp[0] = 0
        # for target in range(1, n + 1):
        #     for s in range (1, target + 1):
        #         square = s * s
        #         if target - square < 0:
        #             break
        #         dp[target] = min(dp[target], dp[target - square] + 1)
        # return dp[n]

        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]