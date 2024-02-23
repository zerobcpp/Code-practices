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
    
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        cd, sell, buy = 0, 0, -prices[0]
        
        for i in range(1, N):
            pcd, ps, pb = cd, sell, buy
            cd = max(pcd, ps)
            buy = max(pcd - prices[i], pb)
            sell = pb + prices[i]
        
        return max(sell, buy, cd)
            