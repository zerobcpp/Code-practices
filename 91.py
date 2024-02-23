class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        elif n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            v1 = int(s[i-1])
            v2 = int(s[i-2:i])
            if 0 < v1 < 10:
                dp[i] += dp[i-1]
            if 10 <= v2 <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
            
        
        
        
