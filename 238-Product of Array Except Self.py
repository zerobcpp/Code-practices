class Solution:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p * nums[i]
            #print(output, p)
        print(output)
        p = 1
        for i in range(n-1, -1, -1):
            output[i] *= p
            p *= nums[i]
            #print(output)
        
        return output