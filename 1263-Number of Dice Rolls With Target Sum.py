class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def helper(left, remain):
            if left <= 0:
                if remain == 0:
                    return 1
                return 0
            ways = 0
            for i in range(1, k+1):
                ways += (helper(left-1, remain - i) % MOD)
            
            return ways % MOD
        
        return helper(n, target)
    
    def numRollsToTarget(self, n, k, target):
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        MOD = 1000000007
        for i in range(1, n+1):
            for j in range(1, target+1):
                if i * k < j:
                    break
                
                for l in range(1, k+1):
                    if j - l >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-l]) % MOD
        
        #print(dp)
        return dp[n][target]
                
                