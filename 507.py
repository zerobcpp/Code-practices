class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        temp = num
        res = []
        while temp > 1:
            cur = temp / 2
            
            if cur % 1 != 0:
                if num % ceil(cur) == 0:
                    res.append(ceil(cur))
                    cur = ceil(cur)
                else:
                    if num % floor(cur) == 0:
                        res.append(floor(cur))
                        cur = floor(cur)
            else:
                if num % cur == 0:
                    res.append(cur)
                    
            #print(temp, cur)        
            temp = cur
            
            
        
        print(res)
        return sum(res) == num