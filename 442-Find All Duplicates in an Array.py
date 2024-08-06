class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = set()
        res = []
        for i in nums:
            if i in c:
                res.append(i)
            c.add(i)
            
        return res
    
    def findDuplicates(self, nums):
        N = len(nums)
        res = [] 
        for i in range(N):
            idx = abs(nums[i]) -1
            if nums[idx] < 0:
                res.append(idx+1)
            else:
                nums[idx] = -nums[idx]
        
        return res