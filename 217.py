class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set(nums)
        print(a)
        return True if len(a)<len(nums) else False