class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
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