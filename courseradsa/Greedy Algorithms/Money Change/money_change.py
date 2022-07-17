# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    num_coins = 0
    while money > 0:
        if money >= 10:
            money -= 10
            num_coins += 1
        elif money >= 5:
            money -= 5
            num_coins += 1
        else:
            money -= 1
            num_coins += 1
    return num_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
