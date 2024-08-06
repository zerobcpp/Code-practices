class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        dec = True
        inc = True
        for i in range(1, N):
            if nums[i-1] > nums[i]:
                inc = False
        
        for i in range(1, N):
            if nums[i-1] < nums[i]:
                dec = False
        
        #print(inc, dec)
        
        return (inc or dec)
        
        
    
