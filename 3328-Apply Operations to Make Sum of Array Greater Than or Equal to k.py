class Solution:
    def minOperations(self, k: int) -> int:
        res = k
        for i in range(1, k+1):
            mul = ceil((k / i)) - 1
            res = min(i-1 + mul, res)         

        
        return res
        