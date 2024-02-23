class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = []
        k = 0
        while nums[k] not in s:
            s = [*s, nums[k]]
            k = nums[k]
            print(s)
        return len(s)