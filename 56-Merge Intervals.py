class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1][1] >= i[0]:
                res[-1] = [min(i[0], res[-1][0]), max(res[-1][1], i[1])]
            else:
                res.append(i)
        
        return res
    
    
    def merge(self, I):
        I.sort(key = lambda x: x[0])
        res = []
        
        for s, e in I:
            if res and res[-1][1] >= s:
                res[-1][0] = min(s, res[-1][0])
                res[-1][1] = max(e, res[-1][1])
            else:
                res.append([s, e])
        
        return res
    
