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

if __name__ == '__main__':
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))