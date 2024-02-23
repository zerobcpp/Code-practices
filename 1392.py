class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        c = set(nums1).intersection(nums2)
        r1 = set()
        r2 = set()
        for i in nums1: 
            if i not in c:
                r1.add(i)
        for i in nums2:
            if i not in c:
                r2.add(i)
        
        return [r1, r2]