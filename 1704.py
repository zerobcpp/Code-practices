class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        N = len(mat)
        M = len(mat[0])
        
        for i in range(M):
            cnt = 0
            for j in range(N):
                if mat[j][i] == 1:
                    cnt += 1
                
                if cnt >= 2:
                    break
            if cnt == 1:
                res += 1
        
        return res
                