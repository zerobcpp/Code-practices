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