# 2466. Count Ways To Build Good Strings
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [-1] * (high)
        mod = 10 ** 9 + 7
        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]
            
        
        return sum(dfs(end) for end in range(low, high + 1)) % mod
    
    
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        res = [1] + [0] * high
        cnt = 0
        for i in range(1, high+1):
            if i >= zero:
                res[i] += res[i-zero]
            if i >= one:
                res[i] += res[i-one]
            res[i] %= MOD
        
        for i in range(low, high+1):
            cnt += res[i]
            cnt %= MOD
        
        return cnt
