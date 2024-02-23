class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r = 0, 0
        ns = len(s)
        nt = len(t)
        res = [False] * ns
        for i in range(ns):
            
            while r < nt:
                found = False
                if t[r] == s[i]:
                    res[i] = True
                    found = True
                r += 1
                if found:
                    break
        
        return True if all(res) else False