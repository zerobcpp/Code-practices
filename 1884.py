class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        res = 0
        i = 1
        while i < N:
            if s[i] == s[i-1]:
                res += 1
                i += 2
                continue
            i += 1
                
        
        return res