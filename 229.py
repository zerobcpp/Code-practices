class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        n = len(nums)
        for i in nums:
            c[i] += 1
        
        res = []
        for i, v in c.items():
            if v > n/3:
                res.append(i)
        
        return res