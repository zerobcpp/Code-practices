class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            cnt = 0
            while i:
                i &= (i-1)
                cnt += 1
            res.append(cnt)
        return res