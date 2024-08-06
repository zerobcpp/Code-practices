class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = -float('inf')
        c = set()
        n = len(nums)
        
        for i in range(n):
            c.add(nums[i][i])
            c.add(nums[i][n - i - 1])
        
        #print(c)
        for cand in c:
            prime = True
            for i in range(2, int(cand ** 0.5)+1):
                if cand % i == 0:
                    prime = False
                    break
            if prime and cand != 1:
                res = max(res, cand)
            
        
        return 0 if res == -float('inf') else res