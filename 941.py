class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e = []
        o = [] 
        
        for i in nums:
            if i & 1 == 0:
                e.append(i)
            else:
                o.append(i)
        
        return e + o
    
    
    def sortArrayByParity(self, nums):
        N = len(nums)
        l = 0
        
        for r in range(N):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums