class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        gridt = [[] for i in range(n)]
        
        res = 0 
        
        for i in range(n):
            for j in range(n):
                same = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        same = False
                        break
                res += same
        
        return res
                
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        gridt = [[] for i in range(n)]
        
        res = 0 
        for i in range(n):
            for j in range(n):
                gridt[i].append(grid[j][i])

        
        c = defaultdict(int)
        for i in grid:
            c[tuple(i)] += 1
        res = 0
        #print(gridt)
        #print(c)
        for i in gridt:
            res += c[tuple(i)]
        
        return res