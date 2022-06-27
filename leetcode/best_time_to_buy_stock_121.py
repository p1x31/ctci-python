def maxProfit(prices) -> int:
    #2179 ms
    max_profit = 0
    current_min = prices[0]

    for i in range(1, len(prices)):
        price = prices[i]
        max_profit = max(max_profit, price - current_min)
        current_min = min(current_min, price)
    return max_profit
    #2034ms
    # if len(prices) < 2:
    #     return 0
    # min_price = prices[0]
    # max_profit = 0
    # for i in range(1, len(prices)):
    #     if prices[i] < min_price:
    #         min_price = prices[i]
    #     elif prices[i] - min_price > max_profit:
    #         max_profit = prices[i] - min_price
    # return max_profit
    # WA shouldnt find the last element
    #return max(prices[prices.index(min(prices)):]) - min(prices)
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))