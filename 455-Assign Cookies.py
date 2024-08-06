class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        print(g, s)
        while g and s:
            greed = False
            if s[-1] >= g[-1]:
                res += 1
                g.pop()
                s.pop()
                greed = True
            if not greed:
                g.pop()
            #print(g,s)
        
        return res
    
    
    def findContentChildren(self, g, s):
        res = 0
        g.sort()
        s.sort()
        i = 0
        j = 0
        n = len(g)
        m = len(s)
        #rint(g, s)
        
        while i < n and j < m:
            
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res
            