class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        N = len(mat)
        st = []
        for i in range(N):
            heappush(st, (sum(mat[i]), i))
        res = []
        while k:
            v, i = heappop(st)
            res.append(i)
            k -= 1
        
        return res