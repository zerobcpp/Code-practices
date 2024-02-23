class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def helper(i, left):
            if left == 0:
                if i == 0:
                    return 1
                else:
                    return 0
            if i >= arrLen or i < 0:
                return 0
            
            count = 0
            count += helper(i+1, left -1) + helper(i-1, left - 1) + helper(i, left-1)
            count %= MOD
            return count
        
        return helper(0, steps)