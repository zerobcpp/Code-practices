class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c)
        return max(c)