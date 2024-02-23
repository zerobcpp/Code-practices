class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = -1
        N = len(heights)
        st = [(0, bricks, ladders)]
        
        while st:
            fl, br, la = st.pop()
            res = max(fl, res)
            
            if la > 0:
                st.append((fl+1, br, la - 1))
            
            if fl + 1 < N and heights[fl] > heights[fl+1]:
                st.append((fl+1, br, la))
            if fl + 1 < N and heights[fl+1] > heights[fl]:
                diff = heights[fl+1] - heights[fl]
                if br >= diff:
                    st.append((fl+1, br-diff, la))
        
        return res