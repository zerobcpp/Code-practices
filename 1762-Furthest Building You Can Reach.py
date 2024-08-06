class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = -1
        N = len(heights)
        st = [(0, bricks, ladders)]
        
        while st:
            fl, br, la = st.pop()
            res = max(fl, res)
            if fl == N-1:
                return N-1
            
            if la > 0:
                st.append((fl+1, br, la - 1))
            
            if fl + 1 < N and heights[fl] > heights[fl+1]:
                st.append((fl+1, br, la))
            if fl + 1 < N and heights[fl] < heights[fl+1]:
                diff = heights[fl+1] - heights[fl]
                if br >= diff:
                    st.append((fl+1, br-diff, la))
            #print(st)
        
        return res
    
    
    def furthestBuilding(self, height, bricks, ladder):
        N = len(height)
        st = []
        res = -1
        for i in range(1, N):
            diff = height[i] - height[i-1]
            if diff <= 0:
                continue
            if diff > 0:
                heappush(st, diff)
            
            if len(st) > ladder:
                bricks -= heappop(st)
            
            if bricks < 0:
                res = i
                break
                
        
        return res - 1 if res != -1 else N - 1
            
            
                             
            