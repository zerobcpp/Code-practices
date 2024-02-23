class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            temp = str(num)
            n = 0
            for i in temp:
                n += int(i)
            
            num = n
        
        return num