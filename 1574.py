class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        return ((nums[-1]-1) * (nums[-2] - 1))
    
    
    def maxProduct(self, nums):
        one = two = -1
        
        for i in nums:
            if i > two:
                one = two
                two = i
            else:
                one = max(i, one)
                
        print(one, two)
        
        return (one-1) * (two-1)