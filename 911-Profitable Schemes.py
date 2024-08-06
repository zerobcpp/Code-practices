class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        N = len(group)
        cache = [[[-1 for i in range(101)] for j in range(101)] for k in range(101)]
        #print(cache)
        MOD = 10**9 + 7
        def helper(idx, p, req):
            if idx == N:
                return req >= minProfit
            if cache[idx][p][req] != -1:
                return cache[idx][p][req]
            res = 0
            res += helper(idx + 1, p, req)
            if p + group[idx] <= n:
                res += helper(idx + 1, p + group[idx], min(req + profit[idx], minProfit))
            
            cache[idx][p][req] = res % MOD
            return cache[idx][p][req]
        
        return (helper(0, 0, 0))
    
    
    def profitableSchemesTEMP(self, n, mp, g, profit):
        MOD = 10 ** 9 + 7
        N = len(g)
        @lru_cache(None)
        def helper(idx, p, req):
            if idx == N:
                return req <= 0
            
            res = helper(idx + 1, p, req)
            if p - g[idx] >= 0:
                res += helper(idx + 1, p - g[idx], min(req - profit[idx], req))
            
            return res % MOD
        
        return helper(0, n, mp)