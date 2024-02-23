class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def helper(x):
            print(x)
            if x <= 0:
                return 0
            
            cnt = float('inf')
            for i in range(1, int(x ** 0.5)+1):
                cnt = min(cnt, helper(x - i ** 2) + 1)
            
            return cnt
        
        return helper(n)
    
    
    def numSquares(self, n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            dp[i] = float('inf')
            
            for j in range(int((i ** 0.5) + 1)):
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])
        
        #print(dp)
        return dp[n]