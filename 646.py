class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        res = []
        
        for s, e in pairs:
            if not res:
                res.append([s, e])
            if s > res[-1][1]:
                res.append([s,e])
        
        return len(res)