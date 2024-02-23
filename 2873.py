class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        res = []
        for i in range(2, n//2 + 1):
            if prime(i) and prime(n-i):
                res.append([i, n-i])
        return res

