class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        N = len(s)
        s.sort()
        def helper(time, idx): 
            if idx == N:
                return 0

            return max(s[idx] * time + helper(time+1, idx+1), 
                        helper(time, idx+1))
        
        return (helper(1, 0))
