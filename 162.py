class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            #rmid = lmid + 1
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid-1]:
                r -= 1
            else:
                l += 1
        
        return -1
            