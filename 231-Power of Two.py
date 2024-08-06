class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n & (n-1) != 0:
            return False
        return True
    
    
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        def helper(num):
            if num % 1 > 0:
                return False
            if num == 1:
                return True
            return helper(num/2)
        
        return helper(n)
    
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return math.log(n, 2) % 1 == 0 or log(n, 2) % 1 <= 1e-10
            
        
        
