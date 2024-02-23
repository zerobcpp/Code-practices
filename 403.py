class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        d = {}
        for i, v in enumerate(stones):
            d[v] = i
        #print(d)
        cache = {}
        
        def helper(i, k):
            #print(i, k)
            if i == N - 1:
                return True
            if (i, k) in cache:
                return cache[i, k]
            can = False
            for j in [k-1, k, k+1]:
                if j > 0 and stones[i] + j in d:
                    if helper(d[stones[i] + j], j):
                        can = True
            cache[i, k] = can
            return can
                    
        
        return helper(0, 1)