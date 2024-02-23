class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = dict(dict.fromkeys(nums, 0))
        res = []
        for i in nums:
            count[i] += 1
        
        for i, j in count.items():
            if j == 1:
                res.append(i)
        
        return res