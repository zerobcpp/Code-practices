# 1844. Replace All Digits with Characters

class Solution:
    def replaceDigits(self, s: str) -> str:
        N = len(s)
        i = 0
        res = []
        for i in s:
            if i.isdigit():
                letter = ord(res[-1]) + int(i)
                res.append(chr(letter))
            else:
                res.append(i)
        
        return ''.join(res)