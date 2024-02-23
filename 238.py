class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in nums]
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                res[i] *= nums[j]
            #print(res)
        
        return res