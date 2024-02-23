class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(time)
        def helper(i, c):
            if c <= 0:
                return 0
            
            if i >= N:
                return float('inf')
            
            t = helper(i+1, c - time[i] - 1) + cost[i]
            nt = helper(i+1, c)

            count = min(t, nt)
            return count
        
        return helper(0, N)
        
            