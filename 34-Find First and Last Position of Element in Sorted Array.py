class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, v in enumerate(nums):
            if v == target:
                res.append(i)
        
        
        if not res:
            return [-1, -1]
        if len(res) == 1:
            return [res[0], res[0]]
        else:
            return [res[0], res[-1]]
    
