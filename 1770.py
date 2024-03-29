class Solution:
    def minDeletions(self, s: str) -> int:
        c = defaultdict(int)
        mx = 0
        for i in s:
            c[i] += 1
            mx = max(mx, c[i])
        
        count = defaultdict(list)
        
        for i, v in c.items():
            count[v].append(i)
        
        res = 0
        for i in range(mx, 0, -1):
            if i in count:
                while len(count[i]) > 1:
                    res += 1
                    count[i-1].append(count[i].pop())
            #print(count)
        
        return res
    
    
    def minDeletions(self, s):
        c = defaultdict(int)
        
        for i in s:
            c[i] += 1
        
        freq = set()
        res = 0
        for i, v in c.items():
            
            while v > 0 and v in freq:
                v -= 1
                res += 1
            freq.add(v)
        
        return res