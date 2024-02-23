class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def helper(i, j):
            if i > j:
                return 0

            if i == j:
                return 1
            if s[i] == s[j]:
                return helper(i+1, j-1) + 2
            else:
                return max(helper(i, j-1), helper(i+1, j))
        n = len(s)
        return helper(0,n-1)