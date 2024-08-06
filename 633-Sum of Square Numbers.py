class Solution:
    def judgeSquareSum(self, c):
        l, r = 0, int(c**0.5) + 1
        
        while l <=  r:
            mid = l + (r-l) // 2
            power = l * l + r * r
            #print(mid, power)
            if power == c:
                return True
            if power < c:
                l += 1
            else:
                r -= 1
        
        return False
            
            