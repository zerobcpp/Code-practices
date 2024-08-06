class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums = [-1] + nums + [-1]
        N = len(nums)
        res = []
        for i in range(1, N-1):
            if nums[i-1] + 1 != nums[i] or nums[i+1]+1 != nums[i]:
                res.append(nums[i])
        
        print(nums, res)
        return res
    
    def findLonely(self, nums):
        c = defaultdict(int)
        
        for i in nums:
            c[i] += 1
        
        res = []
        for i in nums:
            if i-1 not in c and i+1 not in c and c[i] == 1:
                res.append(i)
        
        return res
            