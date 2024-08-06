class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        
        while i < n and j < m: 
            if s[i] == t[j]:
                j += 1
            i += 1
        
        #print(m, j)
        return m - j
        