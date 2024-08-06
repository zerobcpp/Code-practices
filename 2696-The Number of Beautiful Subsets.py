class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        N = len(nums)
        self.res = 0
        def helper(i):
            if i >= N:
                self.res += 1
                return
            
            take = 0
            if c[nums[i] - k] == 0 and c[nums[i] + k] == 0:
                c[nums[i]] += 1
                take = helper(i+1)
                c[nums[i]] -= 1
            ntake = helper(i+1)
            
            
                    
        helper(0)
        
        return self.res - 1
        