class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)
        E = len(s3)
        if N + M != E:
            return False
        @cache
        def helper(i, j):
            if i >= N and j >= M:
                return True
            
            found = False
            if i < N and s1[i] == s3[i+j]:
                if helper(i+1, j):
                    found = True
            if j < M and s2[j] == s3[i+j]:
                if helper(i, j+1):
                    found = True
            
            return found
        
        return helper(0, 0)
            
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)
        E = len(s3)
        if N + M != E:
            return False
        cache = {}
        def helper(i, j):
            if i >= N and j >= M:
                return True
            if (i, j) in cache:
                return cache[i, j]
            found = False
            if i < N and s1[i] == s3[i+j]:
                if helper(i+1, j):
                    found = True
            if j < M and s2[j] == s3[i+j]:
                if helper(i, j+1):
                    found = True
            
            cache[i,j] = found
            return found
        
        return helper(0, 0)
            