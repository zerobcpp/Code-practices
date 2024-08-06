class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            count = 0
            for i in nums:
                count += abs(q - i)
            res.append(count)
        return res
                