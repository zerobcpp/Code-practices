class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        
        @cache
        def helper(i, p):
            print(p)
            if i >= N:
                return 0 if p == 1 else -float('inf')
            
            
            nt = helper(i+1, p) + nums[i]
            t = helper(i+1, 1-p) + (nums[i] ^ k)
            
            return max(t, nt)
        
        return helper(0, 1)
            