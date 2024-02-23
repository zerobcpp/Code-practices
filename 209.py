class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        N = len(nums)
        sm = 0
        res = float('inf')
        for r in range(N):
            sm += nums[r]
            while sm >= target:
                res = min(res, r - l + 1)
                sm -= nums[l]
                l += 1
                
        
        return res if res != float('inf') else 0
    
    
    def minSubArrayLen(self, target, nums):
        pf = [0]
        pf[0] = nums[0]
        for i in nums[1::]:
            pf.append(pf[-1] + i)
        #print(pf)
        
        res = float('inf')
        l = 0
        r = len(nums)
        N = len(pf)
        
        for i in range(N):
            val = pf[i] - target
            if val >= 0:
                idx = bisect_right(pf, val)
                res = min(res, i - idx + 1)
        
        return res if res != float('inf') else 0