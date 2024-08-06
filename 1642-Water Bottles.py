class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        change = numBottles // numExchange
        remaining = (numBottles % numExchange) + change
        
        #print(remaining)
        while remaining >= numExchange:
            remaining -= numExchange
            remaining += 1
            numBottles += 1
        
        
        
        return numBottles + change
        
        
            
            