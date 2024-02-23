class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        c = defaultdict(list)
        for i in arr:
            bits = (bin(i).count('1'))
            c[bits].append(i)
        res = []
        for i in range(15):
            res.extend(c[i])
        
        return res
        
        