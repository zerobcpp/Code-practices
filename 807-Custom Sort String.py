class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = {}
        for i, v in enumerate(order):
            c[v] = i
        
        s = list(s)
        s.sort(key = lambda x: c[x] if x in c else float('inf'))
        return ''.join(s)
    
    
    def customSortString(self, order, s):
        c = defaultdict(int)
        for i in s:
            c[i] += 1
        
        res = []
        
        for i in order:
            if i in c:
                res.append(i * c[i])
                del c[i]
        for i,v in c.items():
            res.append(i * v)
        
        return ''.join(res)