class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        rb = len(matrix)
        cb = len(matrix)
        #res = [[0 for j in range(cb)] for i in range(rb)]

        visited = set()
        from collections import deque
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dirr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x + dirr[0], y + dirr[1]
                if newX >= 0 and newX <= len(matrix) - 1 and newY >= 0 and newY <= len(matrix[0]) - 1 and (
                newX, newY) not in visited:
                    matrix[newX][newY] = matrix[x][y] + 1
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return matrix


if __name__ == '__main__':
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))