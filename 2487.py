class Solution:
    def partitionString(self, s: str) -> int:
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
