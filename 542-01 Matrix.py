class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        pos = [0, 1, 0, -1, 0]
        st = deque()
        visit = set() 
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    st.append((i, j))
                    visit.add((i, j))
        
        while st:
            x, y = st.popleft()
            for i in range(4):
                dx, dy = x + pos[i], y + pos[i+1]
                if 0 <= dx < n and 0 <= dy < m:
                    if (dx, dy) not in visit:
                        visit.add((dx, dy))
                        st.append((dx,dy))
                        mat[dx][dy] = mat[x][y] + 1
        
        return mat
    
    
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        st = deque()
        dirs = [0, 1, 0, -1, 0]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    st.append((i, j))
                else:
                    mat[i][j] = -1
                    
        while st:
            x, y = st.popleft()
            for i in range(4):
                dx, dy = x + dirs[i], y + dirs[i+1]
                if 0 <= dx < n and 0 <= dy < m:
                    if mat[dx][dy] == -1:
                        mat[dx][dy] = mat[x][y] + 1
                        st.append((dx, dy))
        
        return mat