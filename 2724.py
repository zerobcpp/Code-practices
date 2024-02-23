from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = defaultdict(int)
        
        for i in nums:
            c[i] += 1
        res = []
        while c:
            temp = []
            for i, v in c.items():
                temp.append(i)
                c[i] -= 1
            
            res.append(temp)
            for k in list(c.keys()):
                if c[k] == 0:
                    del c[k]
        
        return res