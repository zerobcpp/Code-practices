class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        N = len(job)
        if N < d:
            return -1
        
        @cache
        def helper(i, left, d):
            if i >= N and left <= 0:
                return 0
            if i >= N or left < 0:
                return float('inf')
            
            mx = max(d, job[i])
            keep = helper(i+1, left, mx)
            delete = helper(i+1, left-1, 0) + mx
            
            return min(delete, keep)
        
        return helper(0, d, 0)
                
        