# 2140. Solving Questions With Brainpower
 
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        @cache
        def helper(idx):
            if idx >= N:
                return 0
            count = 0
            pts, bp = questions[idx]
            count = 0
            #print(idx, cd)
            count = max(pts + helper(idx+bp+1), helper(idx+1))
            return count
        
        return helper(0)
    
    def mostPoints(self, qs):
        N = len(qs)
        dp = [0] * N
        
        def helper(idx):
            if idx >= N:
                return 0
            if dp[idx]:
                return dp[idx]
            count = 0
            pts, bp = qs[idx]
            count = max(pts + helper(idx+bp+1), helper(idx+1))
            dp[idx] = count
            return dp[idx]
        
        return helper(0)