class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            if x == -1: 
                continue
            count = 0
            while nums[x] != -1:
                count += 1
                nums[x], x = -1, nums[x]
            res = max(res,count)
        return res