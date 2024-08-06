class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def prime(p):
            if p <= 1:
                return p
            for i in range(2, int((p ** 0.5)+1)):
                if p % i == 0:
                    return False
            
            return True
        
        r = -float(inf)
        n = len(nums)
        for i in range(n):
            if nums[i] < r:
                return False
            else:
                cur = 2
                while cur < nums[i] and (cur <= r or not prime(cur)):
                    cur += 1

                if cur == nums[i]:
                    return False
                else:
                    nums[i] -= cur
                    r = max(r, cur)
        return True
                        