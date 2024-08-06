class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return 0 if n == 0 else 1
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1 
        res[2] = 1
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]
        
        #print(res)
        return res[n]
    
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return 0 if n == 0 else 1
        
        n1 = 0
        n2 = 1
        n3 = 1
        dp = 0
        
        for i in range(3, n+1):
            dp = n3 + n1 + n2
            n1 = n2
            n2 = n3
            n3 = dp
            #print(dp, n1, n2, n3)
        
        return n3
            
            
            
            