class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        @cache
        def helper(i, b):
            if i >= N:
                return 0
            profit = helper(i+1, b)
            if b:
                profit = max(profit, helper(i+1, not b) - prices[i])
            else:
                profit = max(profit, helper(i+2, not b) + prices[i])
            
            return profit
        
        return helper(0, True)
            