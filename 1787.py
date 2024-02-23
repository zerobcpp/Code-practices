class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pf = [nums[0]]
        N = len(nums)
        for i in range(1, N):
            pf.append(pf[-1] + nums[i])
        
        res = []
        for i in range(N):
            left = i
            right = N - i - 1
            
            ls = nums[i] * left - (pf[i] - nums[i])
            rs = (pf[-1] - pf[i]) - nums[i] * right
            
            res.append(ls+rs)
        
        return res