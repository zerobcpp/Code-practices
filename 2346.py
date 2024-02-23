class Solution:
    def largestGoodInteger(self, num: str) -> str:
        N = len(num)
        res = -1
        for i in range(1, N-1):
            if num[i-1] == num[i] == num[i+1]:
                res = max(res, int(num[i]))
        
        return str(res) * 3 if res != -1 else ''