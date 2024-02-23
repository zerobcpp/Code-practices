class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(time)
        cache = {}
        def helper(i, c):
            if c <= 0:
                return 0
            if i >= N:
                return float('inf')
            if (i, c) in cache:
                return cache[i, c]
            
            t = helper(i+1, c - time[i] - 1) + cost[i]
            nt = helper(i+1, c)

            cache[i, c] = min(t, nt)
            return cache[i, c]
        
        return helper(0, N)
        
            