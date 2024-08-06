class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        c = {}
        ct = {}
        for i in range(n):
            si, ti = s[i], t[i]
            if si in c and c[si] != ti:
                return False
            if ti in ct and ct[ti] != si:
                return False
            c[si] = ti
            ct[ti] = si
            
        
        return True