class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        c = list(zip(capital, profits))
        c.sort()
        i = 0
        n = len(c)
        res = w
        st = []
        for _ in range(k):
            while i < n and res >= c[i][0]:
                heappush(st, -c[i][1])
                i += 1
            #print(st)
            if st:
                res -= heappop(st)
            
        
        return res