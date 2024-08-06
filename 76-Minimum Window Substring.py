class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mn = 10 ** 5 + 1
        res = ""
        req = Counter(t)
        
        N = len(s)
        
        cur = req
        l = 0
        for r in range(N):
            
            idx = s[r]
            cur[idx] -= 1
            if all(v <= 0 for v in cur.values()):
                while cur[s[l]] < 0:
                    cur[s[l]] += 1
                    l += 1
                #print(cur)
                
                if r - l < mn:
                    res = s[l:r+1]
                    mn = r - l + 1
        
        return res
                    