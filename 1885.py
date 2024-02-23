class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        res = 0
        cur = 0
        
        for i in range(N):
            if i == 0 or s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            res += cur
            res %= MOD
        
        return res