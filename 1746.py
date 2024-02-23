class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c = defaultdict(list)
        N = len(s)
        for i in range(N):
            c[s[i]].append(i)
            
        res = -1
        for i, v in c.items():
            for i in range(1,len(v)):
                res = max(res, v[i] - v[i-1] - 1)
        
        return res
                
        