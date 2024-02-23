class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return [-1]
        avg = 2 * k + 1
        res = [-1] * n
        val = 0
        for i in range(avg):
            val += nums[i]
        
        res[i-k] = (val//avg)
        l = 0
        for j in range(i+1, n):
            val -= nums[l]
            l += 1
            val += nums[j]
            res[j-k] = (val//avg)
        
        return res
            
            
            