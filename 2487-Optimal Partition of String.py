class Solution:
    def partitionStringn2(self, s: str) -> int:
        n = len(s)
        i = 0
        res = 0
        while i < n:
            temp = {}
            for j in range(i, n):
                idx = s[j]
                if idx not in temp:
                    temp[idx] = 1
                    i += 1
                else:
                    break
            res += 1
        
        return res
    

    def partitionString(self, s):
        n = len(s)
        c = {}
        res = 0
        for i in s:
            idx = i
            if idx in c:
                c = {}
                res += 1
            c[idx] = 1
        
        return res + 1

