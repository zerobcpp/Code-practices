class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        start = intervals[0]
        N = len(intervals)
        res = 0
        for i in range(1, N):
            if intervals[i][0] >= start[1]:
                start = intervals[i]
                res += 1
        
        #print(res)
        return N - res - 1
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        N = len(intervals)
        cur = -float('inf')
        res = 0
        for i in range(N):
            if cur <= intervals[i][0]:
                cur = intervals[i][1]
            else:
                res += 1
        
        return res