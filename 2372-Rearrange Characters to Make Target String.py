class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(target)
        res = float('inf')
        sc = defaultdict(int)
        for i in s:
            sc[i] += 1
        
        for i, v in c.items():
            #print(v, sc[i])
            res = min(res, sc[i]//v)
            
        return res
        