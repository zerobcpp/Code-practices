class Solution:
    def pivotInteger(self, n: int) -> int:
        
        for i in range(1, n+1):
            l = sum(range(1, i+1))
            r = sum(range(i, n+1))
            
            #print(l, r)
            if l == r:
                return i
        
        return -1
    
    
    def pivotInteger(self, n):
        r = None
        for i in range(n+1):
            l = i * (i + 1) / 2
            if r and l == r:
                return i
            r = n * (n + 1) / 2 - l
            
            #print(l, r)
        
        return -1
            