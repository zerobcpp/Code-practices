class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        step = 0
        res = 0
        for i in nums:
            step += i
            if step == 0:
                res += 1
                
        
        #print(step)
        return res
        