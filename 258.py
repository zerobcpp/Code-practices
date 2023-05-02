#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            temp = str(num)
            n = 0
            for i in temp:
                n += int(i)
            
            num = n
        
        return num
    
    def addDigits(self, num):
        n = 0
        while num > 0:
            digit = num % 10
            n += digit
            num //= 10
            
            if n > 9 and num == 0:
                num = n
                n = 0
            #print(num, n)
        
        return n