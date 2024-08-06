class Solution:
    def champagneTower(self, poured: int, row: int, col: int) -> float:
        dp = [[0] * (100) for _ in range(100)]
        dp[0][0] = poured
        
        for i in range(1, row+1):
            for j in range(col+1):
                spill = (dp[i-1][j]-1) / 2
                
                if spill > 0:
                    dp[i][j] += spill
                    dp[i][j+1] += spill
        
        
        #print(dp)
        
        return min(1, dp[row][col])
        