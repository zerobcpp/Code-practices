class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tot1 = 0
        tot2 = 0
        for pow, val in enumerate(list(reversed(num1))):
            pow = int(pow)
            val = int(val)
            tot1 += (val*((10)**pow))
        for pow, val in enumerate(list(reversed(num2))):
            pow = int(pow)
            val = int(val)
            tot2 += (val*((10)**pow))
        #print(tot1,tot2) 
        return str(tot1*tot2)