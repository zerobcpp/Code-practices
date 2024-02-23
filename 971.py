class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        seen = set()
        n = len(grid)
        start = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def search():
            def helper(i, j):
                if i < 0 or j < 0 or i >= n or j >= n or (i, j) in seen or grid[i][j] == 0:
                    return
                start.append((i, j))
                seen.add((i, j))
                for x, y in dirs:
                    helper(i+x, j + y)
                    
                    
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        helper(i, j)
                        return
        
        search()
        res = 0
        #print(start)
        while start:
            m = len(start)
            for _ in range(m):
                x, y = start.popleft()
                for dx, dy in dirs:
                    tdx = x + dx
                    tdy = y + dy
                    
                    if 0 <= tdx < n and 0 <= tdy < n and (tdx, tdy) not in seen:
                        if grid[tdx][tdy] == 1:
                            return res
                        start.append((tdx, tdy))
                        seen.add((tdx, tdy))
            
            res += 1
            
        
        return -1

       
        