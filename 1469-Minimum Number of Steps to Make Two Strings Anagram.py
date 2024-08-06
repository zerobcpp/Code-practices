class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = defaultdict(int)
        
        for i in s:
            c[i] += 1
        
        for i in t:
            c[i] -= 1
            
            
        res = 0
        #print(c)
        for i, v in c.items():
            res += max(0, v)
        return res
    
    # l e e t c o d e
    
            # # 
    # p r a c t i c e
    # x x x t c x x e
    