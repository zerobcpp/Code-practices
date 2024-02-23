class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        
        for i in nums:
            count = 0
            flush = i
            while flush + 1 in nums:
                count += 1
                flush += 1
            
            res = max(count, res)
        
        return res + 1