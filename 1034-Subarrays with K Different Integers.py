class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(k):
            c = defaultdict(int)
            n = len(nums)
            res = 0
            l = 0

            for r in range(n):
                rk = nums[r]
                c[rk] += 1
                while len(c) > k and l < n:
                    lk = nums[l]
                    c[lk] -= 1
                    l += 1
                    if c[lk] == 0:
                        del c[lk]


                res += r - l + 1

            return res
        
        return helper(k) - helper(k-1)
            