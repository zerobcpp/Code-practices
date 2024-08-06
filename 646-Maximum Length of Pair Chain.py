class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort()
        cache = {}
        def helper(i):
            if i >= N:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = 1
            for j in range(i+1, N):
                if pairs[i][1] < pairs[j][0]:
                    cache[i] = max(cache[i], 1 + helper(j))
                    
            return cache[i]
        
        res = 0
        for i in range(N):
            res = max(res, helper(i))
        
        return res
                    
    
    def findLongestChain(self, pairs):
        pairs.sort()
        N = len(pairs)
        dp = [1] * N
        res = 0
        
        
        for i in range(N):
            for j in range(i+1, N):
                if pairs[j][0] > pairs[i][1]:
                    dp[j] = max(dp[i]+1, dp[j])
            res = max(dp[i], res)
        
        return res
    
    
        
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x:x[1])
        #print(pairs)
        cur = -float('inf')
        res = 0
        for s, e in pairs:
            if s > cur:
                cur = e
                res += 1
        
        return res
            