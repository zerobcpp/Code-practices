class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        c = set(words)
        cache = {}
        def helper(w):
            if w in cache:
                return cache[w]
            cnt = 1
            n = len(w)
            for i in range(n):
                word = w[:i] + w[i+1:]
                if word in c:
                    cnt = max(cnt, helper(word) + 1)
            cache[w] = cnt
            return cnt
        
        N = len(c)
        res = 0
        for w in c:
            res = max(res, helper(w))
        
        return res