class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        st = []
        seen = set()
        
        for i in range(n):
            if i not in seen:
                st.append(i)
                seen.add(i)
                while st:
                    cur = st.pop()
                    
                    for j in range(n):
                        if isConnected[cur][j] == 1 and j not in seen:
                            st.append(j)
                            seen.add(j)
                res += 1
        return res