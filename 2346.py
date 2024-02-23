class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        res = ""
        for i in range(1, N-1):
            if num[i-1] == num[i] == num[i+1]:
                res = max(res, num[i-1:i+2])
        
        return res