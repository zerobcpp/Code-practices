class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        N = len(bank)
        M = len(bank[0])
        res = 0
        
        prev = 0
        for i in range(N):
            
            cnt = 0
            for j in range(M):
                if bank[i][j] == '1':
                    cnt += 1
            
            if cnt > 0:
                #print(prev, cnt)
                res += (prev * cnt)
                prev = cnt
        
        return res
                