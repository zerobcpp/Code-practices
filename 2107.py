class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        combination = set(int(i, 2) for i in nums)
        # print(combination)
        for i in range(pow(2, n) - 1, 0, -1):
            if i not in combination:
                return format(i, 'b')
