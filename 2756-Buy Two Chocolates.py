class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        res = money - prices[0] - prices[1]
        
        return res if res >= 0 else money
    
    
    def buyChoco(self, prices, money):
        #print(prices)
        one = two = float('inf')
        
        for i in prices:
            if i < one:
                two = one
                one = i
            elif i < two:
                two = i
        
        res = money - one - two
        
        return res if res >= 0 else money