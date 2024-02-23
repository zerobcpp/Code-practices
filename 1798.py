class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        res = 0
        for i in nums:
            diff = k - i
            if diff in c:
                c[diff] -= 1
                res += 1
            else:
                c[i] += 1
        
        return res