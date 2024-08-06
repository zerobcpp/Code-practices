class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c = {}
        for i in words1:
            c[i] = c.get(i, 0) + 1
        w = {}
        for i in words2:
            w[i] = w.get(i, 0) + 1
        
        res = 0
        for i, v in c.items():
            if c[i] == 1 and w.get(i, 0) == 1:
                res += 1
        
        return res
        
