class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                cnt = 0
                sm = 0
                
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k >= 0 and k < n and l >= 0 and l < m:
                            cnt += 1
                            sm += img[k][l]
            
            res[i][j] = sm // cnt
        
        return res