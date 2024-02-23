class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)
        
        cache = {}
        def helper(r1, r2):
            if r1 < 0 and r2 < 0:
                return 0
            if (r1, r2) in cache:
                return cache[r1, r2]
            if r1 < 0:
                cache[r1, r2] = helper(r1, r2-1) + ord(s2[r2])
                return cache[r1, r2]
            if r2 < 0:
                cache[r1, r2] = helper(r1-1, r2) + ord(s1[r1])
                return cache[r1, r2]
            
            #print(r1, r2)
            if s1[r1] == s2[r2]:
                cache[r1, r2] = helper(r1-1, r2-1)
            else:
                cache[r1, r2] = min(ord(s1[r1]) + helper(r1-1, r2), ord(s2[r2]) + helper(r1, r2-1))
            
            
            return cache[r1, r2]
        
        return helper(N-1, M-1)
                
        
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        @cache
        def helper(r1, r2):
            if r1 < 0 and r2 < 0:
                return 0

            count = float('inf')
            if r1 < 0:
                return helper(r1, r2-1) + ord(s2[r2])
            if r2 < 0:
                return helper(r1-1, r2-1) + ord(s1[r1])
            
            if s1[r1] == s2[r2]:
                return min(count, helper(r1-1, r2-1))
            else:
                return min(ord(s1[r1]) + helper(r1-1, r2), ord(s2[r2]) + helper(r1, r2-1))
            
        
        return helper(N-1, M-1)