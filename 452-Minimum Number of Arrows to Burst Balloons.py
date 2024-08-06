class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        st = []
        res = 1
        print(points)
        for s, e in points:
            if not st:
                st.append(e)
                continue
            if st[-1] < s:
                res += 1
                st.pop()
                st.append(e)
            #print(st)
        
        return res
    
    
    def findMinArrowShots(self, pts):
        pts.sort(key = lambda x:x[1])
        cur = -float('inf')
        res = 0
        for s,e in pts:
            if s > cur:
                cur = e
                res += 1
        
        return res
                