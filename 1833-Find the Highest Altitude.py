class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        ret = 0
        for i in gain:
            ret = max(ret, res[-1] + i)
            res.append(res[-1] + i)
            
        return ret
    
    def largestAltitude(self, gain):
        cur = 0
        res = 0
        for i in gain:
            cur += i
            res = max(cur, res)
        return res
    