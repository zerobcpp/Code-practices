class Solution:
    def numMusicPlaylists(self, N: int, G: int, K: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {}
        def helper(i, j):
            if i == G:
                return 1 if j == N else 0
            if (i, j) in cache:
                return cache[i, j ]
            count = 0
            if j < N:
                count += (N - j) * helper(i+1, j+1) % MOD
            if j > K:
                count += (j - K) * helper(i+1, j) % MOD
            
            cache[i, j] = count
            return count
        
        return helper(0, 0)