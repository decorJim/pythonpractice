"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

# the difference now is that you want to know all the positive slope added together aka total profit you can make
# the sliding window now tracks all upward trend no matter how small

from typing import List


def besttimetobuyandsellstock(prices: List[int]) -> int:

    # you can buy and sell the stock on the same day
    i = 0
    j = 0

    maxProfit = 0
    while j < len(prices):

        # check if it's a upward trend
        if prices[j] - prices[i] > 0:
            maxProfit += prices[j] - prices[i]
            # since selling the stock at day j then you can buy another one after so move i to current day j
            i = j

        if prices[i] > prices[j]:
            i += 1

        else:
            j += 1

    return maxProfit

print(besttimetobuyandsellstock([7,1,5,3,6,4]))
print()

print(besttimetobuyandsellstock([1,2,3,4,5]))
print()

print(besttimetobuyandsellstock([7,6,4,3,1]))
print()


