class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        zR = [0] * n
        zC = [0] * m
        oR = [0] * n
        oC = [0] * m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zR[i] += 1
                    zC[j] += 1
                else:
                    oR[i] += 1
                    oC[j] += 1
        
        #print(oR, oC, zR, zC, end = '\n')
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                res[i][j] = oR[i] + oC[j] - zR[i] - zC[j]
        
        return res
    
    
    
    
    # [2, 2, 1] [1, 1, 3]  1
    # [1, 1, 2] [2, 2, 0]  0