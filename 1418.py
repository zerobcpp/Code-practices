class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        N = len(cookies)
        
        def helper(i, c):
            if N - i < c:
                return float('inf')
            if i >= N:
                return max(cur)
            res = float('inf')
            for j in range(k):
                c -= cur[j] == 0
                cur[j] += cookies[i]
                
                res = min(res, helper(i+1, c))
                cur[j] -= cookies[i]
                c += cur[j] == 0
                
            
            return res
        
        return helper(0, k)