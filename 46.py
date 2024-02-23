class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(nums, path):
            #print(nums)
            print(path)
            if n == len(path):
                res.append(path)
                # return # backtracking
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs(nums, [])
        return res