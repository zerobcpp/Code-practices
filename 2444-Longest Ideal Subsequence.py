class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [[-1] * 128 for _ in range(N)]
        
        def helper(i, prev=None):
            if i >= N:
                return 0
            x = ord(prev)
            #print(x)
            if dp[i][x] != -1:
                return dp[i][x]
            nt = helper(i+1, prev)
            cnt = 0
            if prev == '#':
                cnt = helper(i+1, s[i]) + 1
            elif abs(ord(prev) - ord(s[i])) <= k:
                cnt = max(helper(i+1, s[i]) + 1, cnt)
            
            dp[i][x] = max(cnt, nt)
            return dp[i][x]
        
        return helper(0, '#')
    
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [0] * 26

        res = 0
        # Updating dp with the i-th character
        for i in range(N):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, dp[prev])

            # Append s[i] to the previous longest ideal subsequence
            dp[curr] = max(dp[curr], best + 1)
            res = max(res, dp[curr])
        return res
    
    
                