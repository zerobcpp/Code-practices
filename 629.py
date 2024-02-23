class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def helper(nn, kk):
            if kk <= 0:
                return 1
            
            cnt = 0
            for i in range(nn):
                cnt += (helper(nn - i, kk - i) % MOD)
            
            return cnt
        
        return helper(n, k)
                