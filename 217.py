class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        
        return True if len(nums) > len(n) else False