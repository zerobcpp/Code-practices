class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set()
        s1 = set()
        s2 = set()
        n = len(nums1)
        for i in nums1:
            s1.add(i)
            seen.add(i)
        for i in nums2:
            s2.add(i)
            seen.add(i)
        
        k1 = min(n//2, len(s1))
        k2 = min(n//2, len(s2))
        
        return min(len(seen), k1 + k2)