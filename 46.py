class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        arr = []
        def helper(num):
            if len(arr) == N:
                res.append(arr[:])
                return
            
            for i in range(len(num)):
                arr.append(num[i])
                helper(num[i+1:] + num[:i]) 
                arr.pop()
        
        helper(nums)
        return res
    
    
    def permute(self, nums):
        N = len(nums)
        res = []
        def helper(idx, num):
            if idx == len(num):
                res.append(num[:])
            
            for i in range(idx, N):
                num[idx], nums[i] = nums[i], nums[idx]
                helper(idx+1, num)
                num[idx], nums[i] = nums[i], nums[idx]
            
        helper(0, nums)
        return res