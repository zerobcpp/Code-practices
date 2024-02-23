class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        N = len(num)
        
        for i in range(N):
            if int(num[:i+1]) & 1:
                res = max(res, num[:i+1])
        
        return res