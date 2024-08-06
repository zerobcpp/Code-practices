class Solution:
    def frequencySort1(self, s: str) -> str:
        c = Counter(s)
        count = max(c.values())
        buckets = [[] for i in range(count+1)]
        for i, v in c.items():
            buckets[v].append(i)
        print(buckets)
        res = []
        for i in range(count, -1, -1):
            for c in buckets[i]:
                res.extend(c * i)
        
        return res
            
    
    def frequencySort2(self, s):
        c = Counter(s)
        c = sorted(c.items(), key = lambda x: x[1], reverse = True)
        print(c)
        res = []
        for i, v in c:
            res.extend(i * v)
        
        return res
    
    def frequencySort(self, s):
        c = defaultdict(int)
        mx = 0
        for i in s:
            c[i] += 1
            mx = max(mx, c[i])
        
        cc = defaultdict(list)
        for i, v in c.items():
            cc[v].append(i)
        
        #print(cc)
        res = []
        for i in range(mx, -1, -1):
            if i in cc:
                for v in cc[i]:
                    res.extend(v * i)
        
        return res
    
    def frequencySort(self,s):
        c = Counter(s)
        cc = sorted([(v, i) for i, v in c.items()])
        #print(cc)
        return ''.join(v * i for i, v in cc[::-1])