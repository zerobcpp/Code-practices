class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. 1st method: using the queue shift from python library, deque, numpy
        2. array slicing
        3.
        """
        size = len(nums)
        left = nums[:size-k]
        right = nums[size-k:]
        nums[:] = right + left
        return nums