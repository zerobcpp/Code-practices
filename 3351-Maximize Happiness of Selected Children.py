class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort()
        res = 0
        for i in range(n-1, n-k-1, -1):
            rnds = n - i - 1
            #print(rnds, i, n)
            res += max(happiness[i] - rnds,0)
        
        return res
        