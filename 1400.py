class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0] * 3
        col = [0] * 3
        diag = 0
        rdiag = 0
        
        cnt = 0
        for i, j in moves:
            if cnt == 0:
                player = 1
            else:
                player = -1

            row[i] += player
            col[j] += player
            if i == j:
                diag += player
            if i == 2-j:  
                rdiag += player
            cnt += 1
            cnt %= 2
        
        #print(diag, rdiag, row, col)
        if any(cand == 3 for cand in [row[i], col[j], diag, rdiag]):
            return 'A'
        if any(cand == -3 for cand in [row[i], col[j], diag, rdiag]):
            return 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'