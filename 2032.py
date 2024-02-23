class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        N = len(num)
        
        for i in range(N-1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        
        return res