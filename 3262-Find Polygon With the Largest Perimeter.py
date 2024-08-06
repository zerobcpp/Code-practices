class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        
        pf = [i for i in nums]
        sm = 0
        for i in range(N):
            
            pf[i] -= sm
            sm += nums[i]
        
        #print(pf)
        sm = (nums[0] + nums[1])
        res = -1
        
        for i in range(2, N):
            sm += nums[i]
            if pf[i] < 0:
                res = max(res, sm)
            
            #print(res, sm)
            
        return res
        
            
        

    # [1,12,1,2,5,50,3]
    # [1,1,2,3,5,12,50]