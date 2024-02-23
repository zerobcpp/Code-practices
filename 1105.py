class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        @cache
        def helper(i, j):
            if i >= N or j >= M:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + helper(i+1, j+1)
            else:
                return max(helper(i+1, j), helper(i, j+1))
        
        return (helper(0, 0))