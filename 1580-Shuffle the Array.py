class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        n = len(nums)
        m = n // 2
        for i in range(n//2):
            res.append(nums[i])
            res.append(nums[m+i])
        
        return res
        