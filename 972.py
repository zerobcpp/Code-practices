class Solution:
    def knightDialer(self, n: int) -> int:

        MOD = 10 ** 9 + 7
        moves = {
            0 : [4, 6],
            1 : [8, 6],
            2 : [7, 9],
            3 : [8, 4],
            4 : [9, 3, 0],
            5 : [],
            6 : [1, 7, 0],
            7 : [2, 6],
            8 : [1,3],
            9 : [2, 4],
            '*' : [1,2,3,4,5,6,7,8,9,0]
        }
        
        @cache
        def helper(n, left):
            if left <= 0:
                return 1
            ways = 0
            for neigh in moves[n]:
                ways = (ways + helper(neigh, left-1)) % MOD
            
            return ways
        
        return helper('*', n)
    
    
    def knightDialer(self, n):
        if n == 1:
            return 10
        MOD = 10 ** 9 + 7
        moves = [1] * 10
        moves[5] = 0
        
        for i in range(1, n):
            temp = [0] * 10
            temp[0] = moves[4] + moves[6] % MOD
            temp[1] = moves[8] + moves[6] % MOD
            temp[2] = moves[7] + moves[9] % MOD
            temp[3] = moves[8] + moves[4] % MOD
            temp[4] = moves[3] + moves[9] + moves[0] % MOD
            
            temp[6] = moves[7] + moves[1] + moves[0] % MOD
            temp[7] = moves[2] + moves[6] % MOD
            temp[8] = moves[3] + moves[1] % MOD
            temp[9] = moves[2] + moves[4] % MOD
            moves = temp
        
        #print(moves)
        res = 0
        for i in moves:
            res = (res + i) % MOD
        
        return res
            
            