class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        res = 0
        time = 0
        
        for e, u in customers:
            time = max(time, e)
            
            time += u
            res += time - e
            
            #print(res, time)
            
        
        return res / n