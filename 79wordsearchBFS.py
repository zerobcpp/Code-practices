class Solution:
    def exist(self, board, word: str) -> bool:
        required = len(word) - 1
        n = len(board)
        m = len(board[0])

        start = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    start.append((i, j))

        while start:
            x, y = start.pop(0)
            seen = set()
            seen.add((x, y))
            queue = [(x, y, seen, 0)]
            while queue:
                i, j, seen, count = queue.pop(0)
                if count == required:
                    return True
                # print(i, j, seen, count)
                for dx, dy in ((i + 1, y), (i - 1, y), (x, j - 1), (x, y + 1)):
                    if dx >= 0 and dx < n and dy >= 0 and dy < m:
                        if board[dx][dy] == word[count + 1] and ((dx, dy)) not in seen:
                            print(dx, dy, board[dx][dy], count)
                            # print(dx, dy, seen)
                            copy = seen.copy()
                            copy.add((dx, dy))
                            queue.append((dx, dy, copy, count + 1))
                            print(queue)

        return False


if __name__ == '__main__':
    print(Solution().exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))
    #
    # [["A", "B", "C", "E"],
    #  ["S", "F", "E", "S"],
    #  ["A", "D", "E", "E"]]
    # "ABCESEEEFS"