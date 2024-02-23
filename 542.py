class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rb = len(mat)
        cb = len(mat[0])
        res = []
        for i in range(rb):
            for j in range(cb):
                count = 0
                if mat[i][j] == 0:
                    break
                else:
                    start = (i, j)
                    stack = [start]
                    seen = set()
                    seen.add((i, j))
                    while stack:
                        x, y = stack.pop()
                        for rx, ry in ((i-1, j), (i+1,j), (i, j-1), (i, j + 1)):
                            if (0 <= rx < rb) and (0 <= ry < cb) and (rx, ry) not in seen:
                                if mat[rx][ry] != 0:
                                    stack.append((rx,ry))
                                    seen.add((rx,ry))
                                    count += 1
                                if mat[rx][ry] == 0:
                                    count += 1
                                    break
                    print(i, j, count)
                    if count == 1 and mat[i][j] == 1:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = count - mat[i][j]
        return mat
                                    