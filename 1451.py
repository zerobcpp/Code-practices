class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        res = -1
        N = len(ranges)
        dp = [float('inf')] * N
        dp[0] = 0
        
        for i in range(N):
            neg = max(0, i - ranges[i])
            pos = min(i + ranges[i], n)
            
            for j in range(neg, pos+1):
                dp[pos] = min(dp[j]+1, dp[pos])
        
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1