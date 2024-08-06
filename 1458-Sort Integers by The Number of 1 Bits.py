
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
        
        print(len(c))
        res = []
        for i in range(16):
            res.extend(sorted(c[i]))
        
        return res
        
        