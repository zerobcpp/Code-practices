class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        N = len(cookies)
        ret = float('inf')
        
        def helper(i):
            nonlocal ret
            if i >= N:
                mx = max(cur)
                ret = min(ret, mx)
                return
            if ret <= max(cur): 
                return
            for j in range(k):
                cur[j] += cookies[i]
                helper(i+1)
                cur[j] -= cookies[i]
            
        helper(0)
        return ret
    
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        N = len(cookies)
        def helper(i, val, cur):
            if i >= N:
                return True
            
            for j in range(k):
                if cur[j] + cookies[i] > val:
                    continue
                cur[j] += cookies[i]
                if helper(i+1, val, cur):
                    return True
                cur[j] -= cookies[i]
            
            return False
        
        l = 0
        r = sum(cookies)
        while l <= r:
            mid = l + (r - l) // 2
            cur = [0] * k
            if helper(0, mid, cur):
                r = mid - 1
            else:
                l = mid + 1
            
        return l