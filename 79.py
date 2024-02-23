class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # bfs solution
        m = len(board)
        n = len(board[0]) 
        if not word: 
            return None
        queue = []
        first = word[0]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == first:
                    queue.append((i, j))
                    
        for ix, iy in queue:
            innerqueue = [(ix, iy)]
            innerset = set()
            i = 1
            s = ""
            while innerqueue:
                x, y = innerqueue.pop(0)
                innerset.add((x,y))
                s += board[x][y]
                if s == word:
                    return True
                for dx, dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if (dx >= 0 and dx < m) and (dy >= 0 and dy < n) \
                    and (dx,dy) not in innerset:
                        if board[dx][dy] == word[i]:
                            innerqueue.append((dx, dy))
                i += 1
        
        return False
                