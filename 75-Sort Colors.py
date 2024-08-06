class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
    
    def sortColors(self, nums):

        n = len(nums)
        bucket = [0] * 3
        for i in nums:
            bucket[i] += 1
        
        #print(bucket)
        cur = 0
        for i in range(n):
            while cur < 3 and bucket[cur] == 0:
                cur += 1
            if bucket[cur] > 0:
                nums[i] = cur
                bucket[cur] -= 1
            
            
                
            
            
            
        
                
        
        
            