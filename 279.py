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