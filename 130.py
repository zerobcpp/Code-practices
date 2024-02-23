class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        seen = set()
        n = len(board)
        m = len(board[0])
        st = []
        for i in range(n):
            for j in range(m):
                if (i in [0, n-1] or j in [0, m-1]) and board[i][j] == 'O':
                    st.append((i, j))
                    
        #print(st)
        while st:
            x, y = st.pop()
            board[x][y] = 'f'
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y -1), (x, y + 1)):
                if dx < 0 or dx >= n or dy < 0 or dy >= m:
                    continue
                if (dx, dy) not in seen and board[dx][dy] == 'O':
                    seen.add((dx, dy))
                    st.append((dx, dy))
        
        #print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'f':
                    board[i][j] = 'O'
                else: 
                    board[i][j] = 'X'
        
        return board
                    