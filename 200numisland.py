class Solution:
    def numIslands(self, grid) -> int:
        seen = set()
        stack = []
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in seen:
                    stack.append((i, j))
                    res += 1
                while stack:
                    x, y = stack.pop()
                    seen.add((x, y))

                    for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if (0 <= dx < n) and (0 <= dy < m) and (dx, dy) not in seen and grid[dx][dy] == "1":
                            stack.append((dx, dy))
                            seen.add((dx, dy))

        return res


if __name__ == '__main__':
    print(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))