# 724. Find Pivot Index

class Solution:
    def pivotIndex1(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = [0] * N, [0] * N
        left[0], right[-1] = nums[0],nums[-1]
        for i in range(1,N):
            j = N - i - 1
            left[i] = left[i-1] + nums[i]
            right[j] = right[j+1] + nums[j]
        
        for i, (l,r) in enumerate(zip(left, right)):
            if l == r:
                return i
        return -1
    
    def pivotIndex(self, nums):
        temp = sum(nums)
        left = 0
        idx = 0
        for i in nums:
            if temp - left == i + left:
                return idx
            left += i
            idx += 1
        return - 1