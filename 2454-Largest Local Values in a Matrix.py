class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        
        n = len(grid)
        
        for i in range(n-2):
            res.append([])
            for j in range(n-2):
                mx = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if k < n and l < n:
                            mx = max(mx, grid[k][l])
                
                res[i].append(mx)
        
        return res