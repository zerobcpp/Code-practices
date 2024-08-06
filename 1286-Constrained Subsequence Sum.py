class Solution:
    def constrainedSubsetSum(self, nums: List[int], K: int) -> int:
        st = [(-nums[0], 0)]
        N = len(nums)
        res = cur = nums[0]
        for i in range(1, N):
        
            
            while st and i - st[0][1] > K:
                heappop(st)
            
            
            
            cur = max(0, -st[0][0]) + nums[i]
            res = max(cur, res)
            heappush(st, (-cur, i))
            
            #print(st)
        
        return res
            
            