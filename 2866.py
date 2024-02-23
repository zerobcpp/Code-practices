class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n-1):
            if nums[i] >= threshold:
                continue
            if nums[i] % 2 != nums[i+1] % 2:
                res += 1
        
        return res + 1
                
            