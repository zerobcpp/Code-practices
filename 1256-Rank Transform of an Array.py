class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        c = {}
        res = []
        for i, v in enumerate(sorted(arr)):
            if v in c:
                continue
            c[v] = len(c) + 1
        
        for i in arr:
            res.append(c[i])
        
        return res