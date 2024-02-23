class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        cnt = 0
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                cnt += 1
            res += cnt
        
        return res
                