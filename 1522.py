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
        print(res)
        if res > 0:
            return 'Alice'
        if res < 0:
            return 'Bob'
        else:
            return 'Tie'