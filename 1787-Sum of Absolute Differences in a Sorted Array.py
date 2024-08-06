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
            rs = (pf[N-1] - pf[i]) - nums[i] * right
            
            res.append(ls+rs)
        
        return res
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pf = [nums[0]]
        N = len(nums)
        sm = sum(nums)
        lsm = 0
        res = []
        for i in range(N):
            left = i
            right = N - i - 1
            lsm += nums[i]
            ls = nums[i] * left - (lsm - nums[i])
            rs = (sm - lsm) - nums[i] * right
            
            res.append(ls+rs)
        
        return res