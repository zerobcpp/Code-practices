class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                res += n // 2
                n//=2
            else:
                res += (n-1) // 2 + 1
                n = (n-1) // 2
                
                
            
            #print(res)
        
        return res