class Solution:
    def longestCommonSubSequence(self, t1, t2):
        pass









    def longestCommonSubsequence(self, t1: str, t2: str) -> int: 
        if len(t2) > len(t1):
            t1, t2 = t2, t1
        n = len(t1)
        m = len(t2)
        cache = {}
        def helper(i1, i2):
            if i1 >= n or i2 >= m:
                return 0
            if (i1, i2) in cache:
                return cache[i1, i2]
            if t1[i1] == t2[i2]:
                cache[i1, i2] = 1 + helper(i1+1, i2+1)
            else:
                cache[i1, i2] = max(helper(i1+1, i2), helper(i1, i2+1))
            return cache[i1,i2]
        
        return helper(0,0)
                