class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        c = []
        N = len(dist)
        
#         for d, s in zip(dist, speed):
#             c.append(d/s)
        for i in range(N):
            c.append(dist[i]/speed[i])
        
        res = 0
        c.sort()
        #print(c)
        for i in range(N):
            if c[i] <= i:
                break
            res += 1
        return res