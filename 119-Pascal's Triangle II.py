class Solution:
    def getRow(self, n: int) -> List[int]:
        row = [[1] * (i+1) for i in range(n+1)]
#        print(row)
        
        for i in range(n+1):
            for j in range(1, i):
                row[i][j] = row[i-1][j-1] + row[i-1][j]
        
        
        return row[n]
    
    
    def getRow(self, n):
        prev = [1] * 1
        for i in range(1, n+1):
            dp = [1] * (i+1)
            for j in range(1, i):
                dp[j] = prev[j-1] + prev[j]
            
            
            dp, prev = prev, dp
        
        return prev
            