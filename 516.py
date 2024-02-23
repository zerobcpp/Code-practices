class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        
        @cache
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
    
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        def helper(i, j):
            if i > j:
                return 0
            if (i, j) in cache:
                return cache[i, j]
            if i == j:
                return 1
            if s[i] == s[j]:
                cache[i, j] = helper(i+1, j-1) + 2
            else:
                cache[i, j] = max(helper(i, j-1), helper(i+1, j))

            return cache[i, j]
        n = len(s)
        return helper(0,n-1)
    
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][i] = 1
            for j in range(1, n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        print(dp)
        return dp[n][n-1]
    
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp, prev = [0] * n, [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = prev[j - 1] + 2
                else:
                    dp[j] = max(prev[j], dp[j - 1])
            prev = dp[:]

        return dp[n - 1]