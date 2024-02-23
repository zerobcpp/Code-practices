class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        N = len(s)
        cache = {}
        
        def helper(idx):
            if idx == N:
                return 1
            if s[idx] == '0':
                return 0
            if idx in cache:
                return cache[idx]
            ways = 0
            for i in range(idx, N):
                strs = s[idx:i+1]
                if int(strs) > k:
                    break
                ways += helper(i + 1)
            cache[idx] = ways
            return cache[idx]
        
        helper(0)
        print(cache)
        return cache[0]