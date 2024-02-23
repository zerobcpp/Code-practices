class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1000000000 + 7
        cache = {}
        def helper(i, r, mx):
            if i == n:
                return 1 if r == 0 else 0
            if (i,r, mx) in cache:
                return cache[i,r,mx]
            cnt = helper(i+1, r, mx)
            
            
            for j in range(mx+1, m+1):
                cnt += helper(i+1, r-1, j)
            
            cache[i, r, mx] = cnt
            return cnt
        
        return helper(0, k, 0)