class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        if r == 0:
            return 0
        if r == 1:
            return 1 if nums[1] > nums[0] else 0
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l