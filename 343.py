class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        cache = [-1] * (n+1)
        def helper(remain):
            if remain <= 3:
                return remain
            if cache[remain] != -1:
                return cache[remain]
            cnt = 1
            for j in range(2, remain):
                cnt = max(cnt, j * helper(remain - j))
            cache[remain] = cnt
            return cnt
        
        return helper(n)