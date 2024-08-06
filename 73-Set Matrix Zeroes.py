class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        st = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    st.append((i, j))
        
        while st:
            x, y = st.pop()
            for i in range(n):
                for j in range(m):
                    if i == x:
                        matrix[i][j] = 0
                    elif j == y:
                        matrix[i][j] = 0
            
        return None