class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        nums.sort()

        
        for i in range(n):
            l = nums[i]
            r = l + n - 1
            
            idx = bisect_right(nums, r)
            res = min(res, n - (idx - i))
            #print(l, r, idx)
        
        return res