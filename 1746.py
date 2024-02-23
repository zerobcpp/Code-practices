class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c = defaultdict(list)
        N = len(s)
        for i in range(N):
            c[s[i]].append(i)
            
        res = -1
        #print(c)
        for i, v in c.items():
            
            if len(v) > 1:
                n = len(v)
                res = max(res, v[n-1] - v[0] - 1)
        return res
                
        
        
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c = {}
        N = len(s)
        res = -1
        for i in range(N):
            if s[i] in c:
                res = max(res, i - c[s[i]]-1)
            else:
                c[s[i]] = i
        
        return res
                