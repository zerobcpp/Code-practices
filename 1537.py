class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        right = [0] * n
        
        if s[0] == '0':
            left[0] = 1
        if s[n-1] == '1':
            right[n-1] = 1
        
        
        for i in range(1,n-1):
            if s[i] == '0':
                left[i] = left[i-1] + 1
            else:
                left[i] = left[i-1]
        
        for i in range(n-2, 0, -1):
            if s[i] == '1':
                right[i] = right[i+1] + 1
            else:
                right[i] = right[i+1]
        
        res = 0
        
        for i in range(n):
            res = max(res, left[i]+right[i])
            #print(i, left, right)
        
        return res
            