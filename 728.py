class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for i in range(left, right + 1):
            div = True
            num = i
            while i > 0:
                digit = i % 10
                if digit == 0 or num % digit != 0:
                    div = False
                    break
                i //= 10
            
            if div:
                res.append(num)
                
        return res
                