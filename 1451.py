class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        res = -1
        N = len(ranges)
        for i in range(N):
            neg = i - ranges[i]
            pos = i + ranges[i]
            if neg <= 0 and pos >= n:
                res = i
                break
        
        return res