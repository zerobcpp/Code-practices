class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob = [0] * n
        rob[0], rob[1] = nums[0], nums[1]
        
        for i in range(2, n):
            #print((nums[:i+1:2]), nums[1:i+1:2])
            if i % 2 != 0:
                rob[i] = sum(nums[1:i+1:2])
            else:
                rob[i] = sum(nums[:i+1:2])
            
            
            
        return rob[-1] if rob[-1] > rob[-2] else rob[-2]