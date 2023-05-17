# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
    
    def moveZeroes(self, nums):
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[zero] = nums[i]
                zero += 1
        
        for i in range(zero, n):
            nums[i] = 0
        
        return nums
    
    def moveZeroes(self, nums):
        res = []
        cnt = 0
        for i in nums:
            if i == 0:
                cnt += 1
            else:
                res.append(i)
        
        while cnt:
            res.append(0)
            cnt -= 1
        nums = res
        #print(nums)
        return nums
    
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)