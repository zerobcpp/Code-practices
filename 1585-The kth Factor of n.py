class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, ceil(n ** 0.5)):
            if n % i == 0:
                res.append(i)
            if len(res) > k:
                break
        
        return res[k-1] if len(res) > k-1 else -1
    
    def kthFactor2(self, n, k):
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
            
            if k == 0:
                return i
        
        return -1