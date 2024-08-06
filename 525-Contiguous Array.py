class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c = defaultdict(int)
        N = len(nums)
        cnt = 0
        res = 0
        c[0] = -1
        for r in range(N):
            
            cnt += 1 if nums[r] == 0 else -1
            
            if cnt in c:
                res = max(res, r - c[cnt])
            else:
                c[cnt] = r
            #print(c)
        
        return res
                
            