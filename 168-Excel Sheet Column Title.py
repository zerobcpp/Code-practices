class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        
        while n > 0:
            n -= 1
            cur = n % 26
            n //= 26
            res.append(chr(cur+65))
            
        
        return ''.join(res[::-1])