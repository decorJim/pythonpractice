"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

# the difference now is that you want to know all the positive slope added together aka total profit you can make
# the sliding window now tracks all upward trend no matter how small

from typing import List


def besttimetobuyandsellstock(prices: List[int]) -> int:

    maxProfit = 0

    # front of window starts at 1 but never reaches len(prices)
    for i in range(1,len(prices)):

        # when an upward trend is detected between 2 consecutive days add it to profit
        if prices[i] - prices[i-1] > 0:
            maxProfit += prices[i] - prices[i-1]

    return maxProfit
   

   

print(besttimetobuyandsellstock([7,1,5,3,6,4]))
print()

print(besttimetobuyandsellstock([1,2,3,4,5]))
print()

print(besttimetobuyandsellstock([7,6,4,3,1]))
print()

print(besttimetobuyandsellstock([1, 2, 1, 2, 1, 2, 1, 2]))
print()


