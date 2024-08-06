class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
        
        
        #print(c)
        st = []
        res = []
        for i, v in c.items():
            heapq.heappush(st, heapObj(v, i))
        
        while st:
            cur = heappop(st)
            v, i = cur.f, cur.i
            for i in range(i):
                res.append(v)
        return res
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
            
        bucket = [[] for i in range(101)]
        for i, v in c.items():
            bucket[v].append(i)
        
        res = []
        for i in range(1, 101):
            if bucket[i]:
                for val in sorted(bucket[i], reverse = True):
                    res.extend([val] * i)
        return res
    
    def frequencySort(self, nums):
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
        nums.sort(key = lambda x: (c[x], -x))
        return nums
    

class heapObj:
    def __init__(self, i, f):
        self.i = i
        self.f = f
    
    def __lt__(self, other):
        if self.i == other.i:
            return self.f > other.f
        return self.i < other.i
        
    def __str__(self):
        return f'{self.i} - {self.f}'
            