class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [2*i+start for i in range(n)]
        c = 0
        for i in arr:
            c ^= i
        
        return c