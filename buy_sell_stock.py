def get_global_min(heights):
    global_mins = []
    min = heights[-1]
    for i in reversed(heights):
        if i > min:
            min = i
        global_mins.append(min)
    return list(reversed(global_mins))


def buy_sell(stocks):
    profits = []
    mins = get_global_min(stocks)
    print(mins)
    for i in range(len(stocks)):
        profit = mins[i] - stocks[i]
        profits.append(profit)
    return max(profits)


print(buy_sell([7, 1, 5, 3, 6, 4]))
