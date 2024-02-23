class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for current in output:
                temp.append(current + [num])
            for i in temp:
                output.append(i)
        return output
    
    def subsets(self, nums):
        res = []
        arr = []
        N = len(nums)
        def helper(start, end):

            if len(arr) == end:
                res.append(arr[:])
                return


            for i in range(start, N):
                arr.append(nums[i])
                helper(i+1, end)
                arr.pop()        
        
        for i in range(N+1):
            helper(0, i)
        #print(res)
        
        return res