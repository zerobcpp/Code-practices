class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        nums = list(set(nums))
        nums.sort()
        #rint(nums)
       
        for i in range(len(nums)):
            l = nums[i]
            r = l + n - 1
            
            idx = bisect_right(nums, r)
            res = min(res, n - (idx - i))
            #print(l, r, idx)
        
        return res