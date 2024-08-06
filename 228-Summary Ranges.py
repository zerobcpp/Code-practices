class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        i = 0
        res = []
        while i < N:
            l = r = i
            while r < N-1 and nums[r] + 1 == nums[r+1]:
                r += 1
            if l != r:
                res.append(f'{nums[l]}->{nums[r]}')
            else:
                res.append(str(nums[l]))
            i = r + 1
        
        return res
