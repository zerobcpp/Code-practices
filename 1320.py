class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        
        for i in s:
            if res and res[-1][0] == i:
                res[-1][1] += 1
            else:
                res.append([i, 1])
            if res[-1][1] == k:
                res.pop()
        
        return "".join(i*v for i, v in res)