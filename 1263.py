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