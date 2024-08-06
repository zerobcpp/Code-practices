class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                temp = (nums[i] + nums[i+1]-1) // nums[i+1]
                #print(temp)
                res += temp - 1
                nums[i] //= (temp)
            #print(nums)

        
        return res
                
    
    def minimumReplacement(self, nums):
        N = len(nums)
        prev = nums[-1]
        res = 0
        for i in range(N-2, -1, -1):
            temp = (nums[i] + prev - 1) // prev
            res += temp - 1
            prev = nums[i] // temp
        
        return res
            