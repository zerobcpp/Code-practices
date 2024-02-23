class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        
        def helper(start, num):
            #print(num)
            if num >= low and num <= high:
                res.append(num)
            
            for i in range(start, 10):
                if num * 10 + i <= high:
                    if abs(num % 10 - i) == 1:
                        helper(i+1, num * 10 + i)  
        
        for i in range(1, 10):
            helper(i, i)
        
        res.sort()
        return res