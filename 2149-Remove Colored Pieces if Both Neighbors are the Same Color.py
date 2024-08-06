class Solution:
    def winnerOfGame(self, color: str) -> bool:
        N = len(color)
        a = b = 0
        for i in range(1, N-1):
            if color[i] == color[i-1] == color[i+1] == 'A':
                a += 1
            elif color[i] == color[i-1] == color[i+1] == 'B':
                b += 1
        
        #print(a, b )
        return a > b
                
            