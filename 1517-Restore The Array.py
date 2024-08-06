class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        cache = [-1] * N
        
        def helper(idx):
            if idx == N:
                return 1
            if s[idx] == '0':
                return 0
            if cache[idx] != -1:
                return cache[idx]
            ways = 0
            for i in range(idx, N):
                strs = s[idx:i+1]
                if int(strs) > k:
                    break
                ways += helper(i + 1)
            cache[idx] = ways % MOD
            return cache[idx]
        
        helper(0)
        #print(cache)
        return cache[0]
    
    
    
    #o(n * 9）