
def bestTime(currentProfit, day,prices,items=False):
    if day>=len(prices):
        return currentProfit
    
    buy=bestTime(currentProfit-prices[day],day+1,prices,True)

    cool=bestTime(currentProfit,day+1,prices,items)
    
    if items and prices[day]!=0:
        sell=bestTime(currentProfit+prices[day],day+2,prices,False)
    else:
        sell=float('-inf')
    
    return max(buy,sell,cool)



print(bestTime(0, 0, [0,6,8,6,6,8]))


# def calulateMaxProfitUsingRecursion(prices):

#     def calculateMaxProfit(day):
#         if day < 1:
#             return 0
#         maxProfit = calculateMaxProfit(day-1)
#         for purchaseDay in range(day):
#             if prices[day] > prices[purchaseDay]:
#                 maxProfit = max(maxProfit,prices[day]-prices[purchaseDay]+calculateMaxProfit(purchaseDay-2))
#         return maxProfit
        
#     return calculateMaxProfit(len(prices)-1)


# from collections import defaultdict

# def bestTime(currentProfit, day, prices, memo=defaultdict(float), items=False):
#     key = (currentProfit, day,items)
#     if key in memo:
#         return memo[key]

#     if day >= len(prices):
#         return currentProfit

#     buy = bestTime(currentProfit - prices[day], day + 1, prices, memo, True)
#     cool = bestTime(currentProfit, day + 1, prices, memo, items)
#     sell = float('-inf')
#     if items and prices[day] != 0:
#         sell = bestTime(currentProfit + prices[day], day + 2, prices, memo, False)
#     memo[key] = max(buy, sell, cool)
#     return memo[key]


# def bestTime(prices):
#     if not prices:
#         return 0

#     n = len(prices)
#     buy = [0] * n
#     sell = [0] * n
#     cool = [0] * n

#     buy[0] = -prices[0]

#     for i in range(1, n):
#         buy[i] = max(cool[i-1] - prices[i], buy[i-1])
#         sell[i] = max(buy[i-1] + prices[i], sell[i-1])
#         cool[i] = max(sell[i-1], cool[i-1], buy[i-1])

#     return max(sell[-1], cool[-1],buy[-1])

    
# # Example usage
# prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
# # max_profit = bestTime(0, 0, prices)
# # print(f"Maximum profit: {max_profit}")
# print(bestTime(prices))
# # print(maxProfit(prices))