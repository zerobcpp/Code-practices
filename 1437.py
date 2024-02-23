class Solution:
    def minInsertionscache(self, s: str) -> int:
        n = len(s)
        @cache
        def helper(strs, i, j):
            if i >= n or j < 0:
                return 0
            if strs[i] == strs[j]:
                return 1 + helper(strs, i + 1, j - 1)
            
            return max(helper(strs, i, j-1), helper(strs, i+1, j))
        
        
        
        return n - helper(s, 0, n-1)
    
    def minInsertions(self, s: str) -> int:
        n = len(s)
        cache = {}
        def helper(strs, i, j):
            if i >= n or j < 0:
                return 0
            if (i, j) in cache:
                return cache[i, j]
            if strs[i] == strs[j]:
                cache[i,j] = 1 + helper(strs, i + 1, j - 1)
            else:
                cache[i,j] = max(helper(strs, i, j-1), helper(strs, i+1, j))
            
            return cache[i, j]
        
        
        
        return n - helper(s, 0, n-1)