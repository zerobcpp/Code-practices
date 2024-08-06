class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        n = len(nums)
        sm = 0
        res = 0
        for i in range(n):
            sm += nums[i]
            sm %= k
            if sm == 0:
                res += 1
            res += c[sm]
            c[sm] += 1
            
            #print(c, sm)
        
        return res
            