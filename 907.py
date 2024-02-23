class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        l = 0
        r = max(piles)
        def helper(k):
            hour = 0
            for i in range(N):
                hour += ceil(piles[i]/k)
            
            return hour <= h
        
        ret = 0    
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                ret = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ret
        
        
            