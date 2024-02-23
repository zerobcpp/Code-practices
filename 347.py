class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = set()
        d = {}
        for i in nums: 
            d[i] = d.get(i, 0) + 1
            if d[i] >= k:
                res.add(i)
        
        return res