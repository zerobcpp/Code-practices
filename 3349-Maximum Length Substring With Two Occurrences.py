class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        l = 0
        c = defaultdict(int)
        N = len(s)
        for r in range(N):
            idx = s[r]
            c[idx] += 1
            while c[idx] > 2 and l < N:
                lidx = s[l]
                c[lidx] -= 1
                l += 1
            #print(c, l, r)
            res = max(r - l + 1, res)
        
        return res