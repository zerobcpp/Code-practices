class Solution:
    def minimumPushes(self, word: str) -> int:
        c = {}
        for i in word:
            c[i] = c.get(i, 0) + 1
        
        st = [(-v, i) for i, v in c.items()]
        heapify(st)
        cur = 2
        rounds = 1
        res = 0
        
        while st:
            cnt, idx = heappop(st)
            res += -cnt * rounds
            cur += 1
            if cur > 9:
                cur = 2
                rounds += 1
        
        return res
            
            