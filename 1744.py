class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1e9 + 7
        res = 0
        n = len(words)
        m = len(words[0])
        t = len(target)
        cnt = {}
        
        for i in range(n):
            for i, j in enumerate(words[i]):
                cnt[i, j] = cnt.get((i, j), 0) + 1
        #print(cnt)
        cache = {}
        def helper(i, j):
            if j >= t:
                return 1
            if i >= m:
                return 0
            if (i, j) in cache:
                return cache[i, j]
            res = 0
            jidx = target[j]
            if (i, jidx) in cnt and cnt[i, jidx] > 0:
                res += (cnt[i, jidx] * helper(i + 1, j + 1))
            
            res += helper(i+1, j)
            cache[i,j] = res % MOD
            return cache[i, j]
        
        res = helper(0, 0) % MOD
        #print(cache)
        return int(res)