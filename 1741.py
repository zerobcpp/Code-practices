class Solution:
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
                    for j in range(i):
                        res.append(val)
        
        return res
        
        