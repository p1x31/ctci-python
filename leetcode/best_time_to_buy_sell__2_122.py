class Solution:
    def maxProfit(self, prices) -> int:
        buy = float('-inf')
        #print(buy)
        sell = 0

        for price in prices:
            # when buy sell balance - price - fee if with fee
            next_buy = max(buy, sell - price)
            #print("buy:", next_buy)
            # when sell buy balance + price
            next_sell = max(sell, price + buy)
            #print("sell:", next_buy)

            buy = next_buy
            sell = next_sell
        return sell

l = Solution()
print(l.maxProfit([7,1,5,3,6,4]))