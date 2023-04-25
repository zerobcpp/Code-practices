# 879 profitable schemes

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        N = len(group)
        cache = {}
        MOD = 10**9 + 7
        def helper(idx, p, req):
            if idx == N:
                return req >= minProfit
            if (idx, p, req) in cache:
                return cache[idx, p, req]
            res = 0
            res += helper(idx + 1, p, req)
            if p + group[idx] <= n:
                res += helper(idx + 1, p+group[idx], min(req + profit[idx], minProfit))
            
            cache[idx, p, req] = res % MOD
            return cache[idx,p, req]
        
        #return (helper(0, ?0, ?0))
        return (helper(0, 0, 0))
    
    
    def profitableSchemes???(self, n, mp, g, profit):
        MOD = 10 ** 9 + 7
        N = len(g)
        @cache
        def helper(idx, p, req):
            if idx == N:
                return req <= 0
            
            res = helper(idx + 1, p, req)
            if p - g[idx] >= 0:
                res += helper(idx + 1, p - g[idx], min(req - profit[idx], req))
            
            return res % MOD
        
        return helper(0, n, mp)
    
    