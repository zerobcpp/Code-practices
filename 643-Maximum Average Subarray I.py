class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        n = len(nums)
        count = 0
        for i in range(k):
            count += nums[i]
        
        res = count/k
        
        for i in range(k, n):
            count += nums[i]
            count -= nums[i-k]
            res = max(res, count/k)
        
        return res
            