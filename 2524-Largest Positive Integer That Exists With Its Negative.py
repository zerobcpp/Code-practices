class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        #print(nums)
        while l < r:
            if -nums[l] == nums[r]:
                return nums[r]
            if -nums[l] < nums[r]:
                r -= 1
            else:
                l += 1
            
            #print(l, r)
        
        return -1
    
    def findMaxK(self, nums):
        c = {}
        mx = 0
        for i in nums:
            c[i] = 1
            mx = max(mx, i)
        
        for i in range(mx, -1, -1):
            if -i in c and i in c:
                return i
        
        
        return -1
    
    def findMaxK(self, nums):
        c = set()
        res = -1002
        for i in nums:
            
            if -i in c:
                res = max(abs(i), res)
            
            c.add(i)
        
        return res if res != -1002 else -1
            
        
    
    