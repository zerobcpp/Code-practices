class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
        n = len(s)
        res = []
        for i in range(cnt-1):
            res.append('1')
        for i in range(cnt, n):
            res.append('0')
        if cnt:
            res.append('1')
        return ''.join(res)
    
    def maximumOddBinaryNumber(self, s):
        cnt = 0
        n = len(s)
        for i in s:
            if i == '1':
                cnt += 1
        res = []
        for i in range(n-1):
            if cnt > 1:
                res.append('1')
                cnt -= 1
            else:
                res.append('0')

        if cnt == 1:
            res.append('1')
        else:
            res.append('0')
        
        return ''.join(res)
    
    def maximumOddBinaryNumber(self, s):
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
        n = len(s)
        if cnt == 0:
            return n * '0'
        else:
            return (cnt - 1) * '1' + (n - cnt) * '0' + '1'
        