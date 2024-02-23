class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append(((i, j), 0))
                elif grid[i][j] == 0:
                    seen.add((i, j))
        # processed
        res = 0
        while queue:
            cord, minute = queue.pop(0)
            x, y = cord[0], cord[1]
            seen.add((x, y))
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (0 <= dx < m) and (0 <= dy < n) and (dx, dy) not in seen:
                    grid[dx][dy] = 2
                    queue.append(((dx, dy), minute + 1))
            res = max(minute, res)

        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return res
