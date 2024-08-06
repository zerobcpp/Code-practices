class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = defaultdict(int)
        
        for i in s:
            c[i] += 1
        
        for i in t:
            c[i] -= 1
        
        res = 0
        for i, v in c.items():
            res += abs(v)
        
        return res