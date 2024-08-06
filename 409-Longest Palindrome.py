class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        if len(s) == 1:
            return 1
        c = defaultdict(int)      
        for i in s:
            c[i] += 1
        
        odd = False
        res = 0
        for i,v in c.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                odd = True
        
        
        
        return res+1 if odd else res
                