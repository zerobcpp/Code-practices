class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                temp = (nums[i] + nums[i+1]-1) // nums[i+1]
                #print(temp)
                res += temp - 1
                nums[i] = nums[i] // temp - 1
            print(nums)

        
        return temp
                
                    