def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    1. 1st method: using the queue shift from python library, deque, numpy
    2. array slicing
    3.
    """
    size = len(nums)
    left = nums[0:size - k:]
    right = nums[size - k::]

    return right+left
if __name__ == '__main__':
    print(rotate(self = None, nums = [1,2,3,4,5,6,7], k = 3))