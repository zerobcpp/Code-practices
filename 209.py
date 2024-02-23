class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        N = len(nums)
        sm = 0
        res = float('inf')
        for r in range(N):
            sm += nums[r]
            while sm > target:
                sm -= nums[l]
                l += 1
                
            #rint(r, l, sm)
            if sm == target:
                res = min(res, r - l + 1)
        
        return res if res != float('inf') else 0
            
            