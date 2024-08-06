class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        
        for i in nums:
            count = 0
            flush = i
            if flush - 1 not in nums:
                count = 1
                while flush + 1 in nums:
                    flush += 1
                    count += 1
            res = max(res, count)
        
        return res