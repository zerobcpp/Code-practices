class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True for i in range(n+1)]
        def sieve():
            nonlocal prime
            p = 2
            while (p * p <= n):

                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
        
        sieve()
        res = []
        for i in range(2, n//2 + 1):
            if prime[i] and prime[n-i]:
                res.append([i, n-i])
        
        return res
