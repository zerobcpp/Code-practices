class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for i in n:
            res = max(res, int(i))
        
        return res
    
    
    def minPartitions(self, n):
        return max(map(lambda x: int(x), n))