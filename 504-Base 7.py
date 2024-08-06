class Solution:
    def convertToBase7(self, nums: int) -> str:
        if nums < 0:
            return "-" + self.convertToBase7(-nums)
        if nums < 7:
            return str(nums)
        return self.convertToBase7(nums//7) + str(nums%7)