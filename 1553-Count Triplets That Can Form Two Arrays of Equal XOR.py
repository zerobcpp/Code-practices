class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pf = [0]
        for i in arr:
            pf.append(pf[-1] ^ i)
        
        n = len(pf)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if pf[i] == pf[j]:
                    res += (j - i -1)
        
        return res