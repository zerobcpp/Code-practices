class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a
        
        while b != 0:
            carry = (a & b) << 1
            a ^= b
            b = carry
        
        return a