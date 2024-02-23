class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def helper(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0 or j > i:
                return 0
            count = 0
            
            count += (i - j) * helper(i-1, j) % MOD
            count += j * helper(i, j-1) % MOD
            
            return count
        
        return helper(n, n)