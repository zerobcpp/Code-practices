class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        c = {}
        sm = sum(nums)
        c[sm] = 1
        res = 0
        for i in range(n):
            target = n - i
            if target in c:
                res += 1
            else:
                c[target] = 1
        
        return res
            
        
        
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result
