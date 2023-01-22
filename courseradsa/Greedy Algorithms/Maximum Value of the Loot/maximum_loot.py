# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    #pseudo
    # if capacity == 0 or len(weights) == 0:
    #     return 0
    # m = weights[0]
    # amount = min(weights[m], capacity) 
    # value = prices[m] * amount / weights[m]
    # weights.pop()
    # prices.pop()
    # return value + maximum_loot_value(capacity, weights, prices)
    cost_weight = {}
    total = 0
    for i in range(len(weights)):
        cost_weight[i] = prices[i] / weights[i]
    
    cost_weight = dict(sorted(cost_weight.items(), key=lambda item: item[1], reverse=True))

    for key, sorted_ratio in cost_weight.items():
        if capacity - weights[key] >= 0:
            capacity -= weights[key]
            total += prices[key]
        else:
            rest = prices[key] * (capacity / weights[key])
            total += rest
            break
    return total

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
