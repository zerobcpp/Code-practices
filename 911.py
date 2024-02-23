class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        res = []
        N = len(group)
        cache = {}
        MOD = 1e9 + 7
        def helper(idx, p, req):
            
            if idx == N:
                return req <= 0
            if p < 0:
                return 0
            if (idx, p, req) in cache:
                return cache[idx, p, req]
            
            res = 0
            res += helper(idx + 1, p, req)
            if p - group[idx] >= 0:
                res += helper(idx + 1, p - group[idx], req - profit[idx])
            
            cache[idx, p, req] = res % MOD
            return cache[idx,p, req]
        
        return int(helper(0, n, minProfit))
        