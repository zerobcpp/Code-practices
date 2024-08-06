class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        c = []
        MOD = 10 ** 9 + 7 
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += nums[j]
                c.append(cnt)
        
        
        c.sort()
        res = 0
        for i in range(left-1, right):
            res += c[i]
            res %= MOD
        
        return res