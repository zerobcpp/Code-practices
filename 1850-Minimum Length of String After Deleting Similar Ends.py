class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        l, r = 0, N-1
        res = N
        cur = N
        while l < r:
            ##print(s[l], s[r])
            if s[l] != s[r]:
                break
            else:
                for i in range(l+1, r):
                    if s[l] != s[i]:
                        break
                    l = i
                for j in range(r-1, -1, -1):
                    if s[r] != s[j]:
                        break
                    r = j
                r -= 1
                l += 1
                if r < l:
                    return 0
                #print(l, r)
                cur = r - l + 1
                res = min(cur, res)
            
            
            
                
                
        
        return res