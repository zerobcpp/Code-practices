class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0 
        N = len(intervals)
        
        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < N and newInterval[1] >= intervals[i][0]:
            s, e = intervals[i]
            newInterval[0] = min(s, newInterval[0])
            newInterval[1] = max(e, newInterval[1])
            i += 1
        
        res.append(newInterval)
        res.extend(intervals[i:])
        #print(i,res)
        return res
    
    
    def insert(self, interval, newInterval):
        res = []
        check = False
        
        for s, e in interval:
            if e < newInterval[0]:
                res.append([s,e])
            elif s > newInterval[1]:
                if not check:
                    res.append(newInterval)
                    check = True
                res.append([s,e])
                
            else:
                newInterval[0] = min(s, newInterval[0])
                newInterval[1] = max(e, newInterval[1])
        
        if not check:
            res.append(newInterval)
        
        return res