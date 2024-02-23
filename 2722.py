class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = -float('inf')
        c = set()
        n = len(nums)
        
        for i in range(n):
            c.add(nums[i][i])
            c.add(nums[i][n - i - 1])
        
        res = max(c)
        for i in range(2, ceil(res ** 0.5)):
            if res % 2 == 0:
                return 0
        
        return res