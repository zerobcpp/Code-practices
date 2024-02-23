# 1870. Minimum Speed to Arrive on Time

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        N = len(dist)
        if ceil(hour) < N:
            return -1
        
        def helper(m):
            speed = 0
            for i in range(N):
                hs = dist[i] / m
                speed += ceil(hs) if i != N-1 else hs
            
            #print(speed)
            return speed <= hour
        
        l, r = 1, 10 ** 9
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
                