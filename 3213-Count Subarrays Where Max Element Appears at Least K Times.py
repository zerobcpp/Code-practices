class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        l = 0
        c = defaultdict(int)
        res = 0
        cnt = 0
        for r in range(n):
            rk = nums[r]
            c[rk] += 1
            
            while c[mx] >= k:
                lk = nums[l]
                c[lk] -= 1
                l += 1
                cnt += 1
            
            res += cnt
            
            #print(c)
        
        return res
            
                
            