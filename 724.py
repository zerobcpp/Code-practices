class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0], right[-1] = nums[0], nums[-1]
        for i in range(1,n):
            j = n - i - 1
            left[i] = left[i-1] + nums[i]
            right[j] = right[j+1] + nums[j]
        
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1