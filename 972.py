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