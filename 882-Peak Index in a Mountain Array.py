class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return -1
        
        l, r = 0, n - 1
        while l < r:
            mid = l + (r-l) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            if arr[mid] > arr[mid-1]:
                l += 1
            else:
                r -= 1
        
        return -1