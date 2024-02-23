class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    
    def climbStairs(self, n):
        p1 = 1
        p2 = 1
        cur = 0
        for i in range(2, n+1):
            cur = p1 + p2
            p1 = p2
            p2 = cur
        
        return p2