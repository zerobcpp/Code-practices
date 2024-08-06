class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = {}
        mx = 0
        for i in nums:
            c[i] = c.get(i, 0) + 1
        
        bucket = defaultdict(list)
        for i, v in c.items():
            bucket[v].append(i)
            mx = max(v, mx)
        
        for i in range(mx, -1, -1):
            if i in bucket:
                return len(bucket[i]) * i
        
        return -1