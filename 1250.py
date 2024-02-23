class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        res = 0
        n = len(t1)
        m = len(t2)
        if m < n:
            t1, t2 = t2, t1
            n, m = m, n

        for i in range(n):
            temp = 1 if t1[i] == t2[i] else 0
            for j in range(i, m):
                if t1[temp] == t2[j]:
                    temp += 1
            
            res = max(res, temp)
        
        return res
