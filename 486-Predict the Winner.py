class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        
        @cache
        def helper(l, r):
            if l == r:
                return nums[l]
            
            left = nums[l] - helper(l+1, r)
            right = nums[r] - helper(l, r-1)
            #print(left, right, l, r)
            return max(left, right)
        
        #print(helper(0, N-1))
        
        return helper(0, N-1) >= 0
        
        