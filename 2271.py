class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
        
        print(p, n)
        np, nn = len(p), len(n)
        ptr = 0
        res = []
        while ptr < np:
            res.append(p[ptr])
            res.append(n[ptr])
            ptr += 1
        
        return res