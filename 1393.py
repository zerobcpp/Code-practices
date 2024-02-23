class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        cache = {}
        def helper(idx, n):
            if idx == 0:
                return 0
            if (idx, n) in cache:
                return cache[idx, n]
            cache[idx, n] = 0
            x = 0
            for i in range(min(n, len(piles[idx-1]))+1):
                if i > 0:
                    x += piles[idx - 1][i - 1]
                
                cache[idx, n] = max(cache[idx, n], helper(idx-1, n - i) + x)
            
            return cache[idx, n]
        
        return helper(n, k)