class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 1<=len(prices)<=pow(10,5):
           i,maxProfit=0,0
           j=i+1
           while j<len(prices):
               if prices[j]-prices[i]>maxProfit:
                   maxProfit=prices[j]-prices[i]
               if prices[i]>prices[j] and i<len(prices)-1:
                   i+=1
                   j=i+1
               else:
                   j+=1
           return maxProfit
        return 0