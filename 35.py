class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if target > nums[right]:
            return right + 1
        elif target == nums[mid]:
            return mid
        else:
            return 0