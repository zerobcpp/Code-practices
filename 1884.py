class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        res = 10 ** 4 + 1
        i = 0
        
        while i <= 1:
            p = i
            cnt = 0
            for j in range(N):
                if int(s[j]) != p:
                    #print(s[i], p, i)
                    cnt += 1
                p += 1
                p %= 2
            #print(cnt, i)
            res = min(res, cnt)
            i += 1
        
        return res
    
    def minOperations(self, s):
        N = len(s)
        res = N
        
        cnt = 0
        for i in range(N):
            if i % 2 == 0:
                if s[i] == '0':
                    cnt += 1
            else:
                if s[i] == '1':
                    cnt += 1
                
        
        return min(res - cnt, cnt)