class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        l = r = 0
        sm = sum(nums)
        target = sm - x
        #nums.sort()
        cur = 0
        res = -float('inf')
        #print(target, sm)
        
        for r in range(N):
            cur += nums[r]
            #print(cur)
            while cur > target and l <= r:
                cur -= nums[l]
                l += 1
            if cur == target:
         #       print(l, r)
                res = max(res, r - l + 1)
            
            
            
            
        
        return N - res if res != -float('inf') else -1