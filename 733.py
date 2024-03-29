class Solution:
    def floodFill1(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        # base case:
        if image[sr][sc] == newColor:
            return image
        target = image[sr][sc]
        self.flood(image, sr, sc, target, newColor)
        return image

    def flood(self, arr, r, c, target, goal):
        rb = len(arr)
        cb = len(arr[0])

        if r < 0 or r >= rb or c >= cb or c < 0:
            return
        elif arr[r][c] != target:
            return
        arr[r][c] = goal
        self.flood( arr, r + 1, c, target, goal)
        self.flood( arr, r - 1, c, target, goal)
        self.flood( arr, r, c + 1, target, goal)
        self.flood( arr, r, c - 1, target, goal)

    
    def floodFill(self, image, sr, sc, nc):
        stack = [(sr, sc)]
        m = len(image)
        n = len(image[0])
        seen = set()
        seen.add((sr, sc))
        goal = image[sr][sc]
        while stack:
            x, y = stack.pop()
            image[x][y] = nc
            for dx, dy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if 0 <= dx < m and 0 <= dy < n:
                    if image[dx][dy] == goal and (dx, dy) not in seen:
                        stack.append((dx, dy))
                        seen.add((dx, dy))
        
        return image