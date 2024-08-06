class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        
        for i in range(N):
            for add in range(2):
                l = i
                r = i + add
                
                while l >= 0 and r < N and s[l] == s[r]:
                    #print(s[l:r+1])
                    res += 1
                    l -= 1
                    r += 1
        
        return res
                