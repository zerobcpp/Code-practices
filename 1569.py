class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        n = len(nums1)
        m = len(nums2)
        cache = {}
        
        def helper(i, j):
            if i >= n or j >= m:
                return 0
            if (i, j) in cache:
                return cache[i, j]
            t = nums1[i] * nums2[j] + helper(i+1, j+1)
            dt = helper(i, j+1)
            skip = helper(i+1, j)
            cache[i, j] = max(t, dt, skip)
            return cache[i, j]
        
        
        return helper(0, 0)