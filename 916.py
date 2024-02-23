class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        res = []
        
        for i in s:
            if len(res) > k:
                return res[k-1]
            if i.isalpha():
                res.append(i)
            else:
                res *= int(i)
        #print(''.join(res))
        return res[k-1]
                