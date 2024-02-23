# 2707. Extra Characters in a String

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        self.res = N = len(s)
        dp = [float('inf')] * (N+1)
        dp[0] = 0
        
        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1
            
            for left in range(1, i+1):
                
                if s[i-left:i] in words:
                    dp[i] = min(dp[i], dp[i-left])
        
        print(dp)
        return dp[-1]
                