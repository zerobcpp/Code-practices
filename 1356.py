# 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        c = defaultdict(list)
        for i in arr:
            temp = i
            bits = 0
            while i > 0:
                i &= i - 1
                bits += 1
            #print(bits)
            c[bits].append(temp)
        res = []
        for i in range(10):
            res.extend(sorted(c[i]))
        
        return res
        
        