class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = {}
        for i in s:
            c[i] = c.get(i, 0) + 1
        
        for i,v in enumerate(s):
            if c[v] == 1:
                return i
        
        return -1
        