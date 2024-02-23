class Solution:
    def myPow(self, x: float, n: int) -> float:
        multipler = 1
        store = n
        n = abs(n)
        for i in range(0, n):
            multipler *= x
        if store >= 0:
            return float(multipler)
        else:
            return float(1/multipler)
