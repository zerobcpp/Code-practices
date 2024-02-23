class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = set()
        for i in nums1:
            if i in nums2:
                count.add(i)
        return [i for i in count]