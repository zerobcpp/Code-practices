class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a
        
        while b != 0:
            carry = (((a & b) << 1) & 0xffffffff)
            a = (a^b) & 0xffffffff
            b = carry
        
        return a if a < 0x7fffffff else ~(a^0xffffffff)