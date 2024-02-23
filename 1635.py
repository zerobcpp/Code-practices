class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = defaultdict(list)
        res = 0
        for i, v in enumerate(nums):
            res += len(c[v])
            c[v].append(i)
        
        return res
            