# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = max(arr)
        return arr.index(n)
    
    def peakIndexInMountainArray(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] > nums[mid]:
                r = mid
            else:
                l = mid + 1
            #print(mid)
        return -1
    

