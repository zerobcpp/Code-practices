class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        res = [[0] * m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                unit = min(rowSum[i], colSum[j])
                res[i][j] = unit 
                rowSum[i] -= unit
                colSum[j] -= unit
        
        return res