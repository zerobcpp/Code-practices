class Solution:
    def canPlaceFlowers(self, flower: List[int], n: int) -> bool:
        N = len(flower)
        flower = [0] + flower + [0]
        res = 0
        for i in range(1, N):
            if flower[i] == 0 and flower[i-1] == 0 and flower[i+1] == 0:
                flower[i] = 1
                res += 1
        
        return res >= n
        