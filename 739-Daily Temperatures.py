class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        N = len(temp)
        res = [0] * N
        st = []
        
        for i, v in enumerate(temp):
            
            while st and st[-1][1] < v:
                idx, val = st.pop()
                res[idx] = i - idx
            
            st.append([i, v])
            
        
        return res