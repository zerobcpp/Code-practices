class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(1, n):
            res += abs(ord(s[i]) - ord(s[i-1]))
            
        
        return res
    
    def scoreOfString(self, s: str) -> int:
        res = 0
        for a, b in pairwise(s):
            res += abs(ord(a) - ord(b))
        
        return res
            