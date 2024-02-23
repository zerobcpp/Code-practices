class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        i = 0
        j = 0
        
        while i < len(g) and j < len(s):
            if s[i] >= g[j]:
                res += 1
            i += 1
            j += 1
        
        return res