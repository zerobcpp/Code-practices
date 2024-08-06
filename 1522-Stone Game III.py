class Solution:
    def stoneGameIII(self, SV: List[int]) -> str:
        N = len(SV)
        @cache
        def helper(idx):
            if idx >= N:
                return 0
            stone = SV[idx] - helper(idx+1)
            
            if idx + 2 <= N:
                stone = max(stone, SV[idx] + SV[idx+1] - helper(idx+2))
            if idx + 3 <= N:
                stone = max(stone, SV[idx] + SV[idx+1] + SV[idx+2] - helper(idx+3))
            
            
            return stone
        
        res = helper(0)
        #print(res)
        if res > 0:
            return 'Alice'
        if res < 0:
            return 'Bob'
        else:
            return 'Tie'
        
    def stoneGameIII(self, SV: List[int]) -> str:
        N = len(SV)
        cache = {}
        def helper(idx):
            if idx >= N:
                return 0
            if idx in cache:
                return cache[idx]
            stone = SV[idx] - helper(idx+1)
            if idx + 2 <= N:
                stone = max(stone, SV[idx] + SV[idx+1] - helper(idx+2))
            if idx + 3 <= N:
                stone = max(stone, SV[idx] + SV[idx+1] + SV[idx+2] - helper(idx+3))
            
            cache[idx] = stone
            return cache[idx]
        
        res = helper(0)
        #print(cache)
        if res > 0:
            return 'Alice'
        if res < 0:
            return 'Bob'
        else:
            return 'Tie'
        
    def stoneGameIII(self, SV):
        N = len(SV)
        dp = [0] * (N+1)
        
        for i in range(N-1, -1, -1):
            dp[i] = SV[i] - dp[i+1]
            if i + 2 <= N:
                dp[i] = max(dp[i], SV[i] + SV[i+1] - dp[i+2])
            if i + 3 <= N:
                dp[i] = max(dp[i], SV[i] + SV[i+1] + SV[i+2] - dp[i+3])
        
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
                
        