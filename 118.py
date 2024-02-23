class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res = []
        for i in range(N):
            level = [1] * (i+1)
            for j in range(1, i):
                level[j] = res[i-1][j] + res[i-1][j-1]
            res.append(level)
        return res
