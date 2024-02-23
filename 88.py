class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort()
        nums2.sort()
        for i in nums2:
            nums1.append(i)
        
        nums1.sort()
        nums1.reverse()
        while len(nums1)>m+n:
            nums1.pop()
        
        nums1.reverse()