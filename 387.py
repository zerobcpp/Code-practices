class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = defaultdict(list)
        
        for i,v in enumerate(s):
            c[v].append(i)
        
        #print(c)
        for i,v in c.items():
            if len(v) == 1:
                return v[0]
            
        return -1
    
    def firstUniqChar(self, s):
        c = defaultdict(int)
        
        for i in s:
            c[i] += 1
        
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        
        return -1