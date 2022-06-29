class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x ^ -n = 1 / (x ^ n)
        def myPowHelper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            #deal with odd numbers
            res = myPowHelper(x * x, n // 2)
            return res if n % 2 == 0 else res * x
            # if n == 1:
            #     return x
            # if n % 2 == 0:
            #     return myPowHelper(x * x, n // 2)
            # else:
            #     return x * myPowHelper(x * x, n // 2)
        res = myPowHelper(x, abs(n))
        return res if n >= 0 else 1 / res
       