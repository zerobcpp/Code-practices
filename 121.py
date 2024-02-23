class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = sys.maxsize
        profit = 0
        
        for i in prices:
            if i < mini:
                mini = i
            elif i - mini > profit:
                profit = i - mini
        
        return profit