class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        count = max(c.values())
        buckets = [[] for i in range(count+1)]
        for i, v in c.items():
            buckets[v].append(i)
        print(buckets)
        res = []
        for i in range(count, -1, -1):
            res.extend((buckets[i] * i))
        
        return res
            