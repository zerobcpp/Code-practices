class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        c = defaultdict(int)
        
        for i in nums:
            res += c[i]
            c[i-k] += 1
            c[i+k] += 1
        
        
        return res