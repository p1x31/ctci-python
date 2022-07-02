class Solution:
    def reverse(self, x: int) -> int:
        #36ms
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        #0x7FFFFFFF is a number in hexadecimal (2,147,483,647 in decimal)
        return result if result <= 0x7fffffff else 0
        #80ms
        # res = 0
        # if x < 0:
        #     res = -int(str(-x)[::-1])
        #     return res if abs(res) <= 0x7fffffff else 0
        # else:
        #     res = int(str(x)[::-1])
        #     return res if res <= 0x7fffffff else 0