class Solution:
    def canPlaceFlowers(self, flower: List[int], n: int) -> bool:
        N = len(flower)
        flower = [0] + flower + [0]
        res = 0
        for i in range(1, N+1):
            if flower[i] == 0 and flower[i-1] == 0 and flower[i+1] == 0:
                flower[i] = 1
                res += 1
        print(flower)
        return res >= n
    
    def canPlaceFlowers(self, flower, n):
        N = len(flower)
        res = 0
        if N == 1 and flower[0] == 0:
            return 1 >= n
        if flower[-1] == 0 and flower[-2] == 0:
            flower[-1] = 1
            res += 1
        if flower[0] == 0 and flower[1] == 0:
            flower[0] = 1
            res += 1
        for i in range(1, N-1):
            if flower[i] == 0 and flower[i-1] == 0 and flower[i+1] == 0:
                flower[i] = 1
                res += 1
            
        return res >= n