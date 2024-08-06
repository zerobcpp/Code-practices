class Solution:
    def threeConsecutiveOdds(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = 0
        cnt = 0
        for l in range(n):
            if nums[l] % 2 != 0:
                sm = 0
                cnt = 0
                r = l
                while r < n and r <= l + 2:
                    sm += nums[r]
                    r += 1
                    cnt += 1
            
            
            if sm % 2 != 0 and cnt == 3:
                return True
        
        return False
    
    
    def threeConsecutiveOdds(self, nums):
        cnt = 0
        n = len(nums)
        for r in range(n):
            if nums[r] & 1 == 1:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == 3:
                return True
        
        return False
    
    def threeConsecutiveOdds(self, nums):
        n = len(nums)
        
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] & 1 == 1: 
                return True
#             if nums[i] * nums[i+1] * nums[i+2] & 1 == 1:
#                 return True
        
        return False