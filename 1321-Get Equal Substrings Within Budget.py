class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = 0
        l = 0
        for r in range(N):
            rs, rt = s[r], t[r]
            cost = abs(ord(rs)-ord(rt))
            maxCost -= cost
            while maxCost < 0:
                ls, lt = s[l], t[l]
                add = abs(ord(ls) -ord(lt))
                maxCost += add
                l += 1
            
            res = max(r - l + 1, res)
            
        
        return res
            
            