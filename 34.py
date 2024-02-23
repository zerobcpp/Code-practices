class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        for i, v in enumerate(nums):
            if v == target:
                res.append(i)
        
        return [-1, -1] if not res else res
                