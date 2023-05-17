# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        point = -100
        for i in gain:
            res.append(res[-1] + i)
            res = max(res, i + res[-1])
        return max(res)
    
    def largestAltitude(self, gain):
        cur = 0
        res = 0
        
        for i in gain:
            cur += i
            res = max(cur, res)
        
        return res
    