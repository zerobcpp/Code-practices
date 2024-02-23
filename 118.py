class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = []
        
        for i in range(n):
            temp = [1] * (i+1)
            for j in range(1, i):
                temp[j] = res[i-1][j] + res[i-1][j-1]
            
            res.append(temp)
        
        return res