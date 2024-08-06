class Solution:
    def countPairs(self, arr: List[int]) -> int:
        c = defaultdict(int)
        MOD = 10 ** 9 + 7
        res = 0
        for i in arr:
            for j in range(25):
                res += c[2 ** j - i]
                res %= MOD
                
            c[i] += 1

        
        return res