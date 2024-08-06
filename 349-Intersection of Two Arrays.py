class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = set()
        for i in nums2:
            if i in c1 and i in c2:
                res.add(i)
        
        return res
    
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)
    
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return s1.intersection(s2)
    
    
    def intersection(self, nums1, nums2):
        c = {}
        
        for i in nums1:
            c[i] = 1
        
        for i in nums2:
            if i in c:
                c[i] = 2
        
        res = []
        for i, v in c.items():
            if v == 2:
                res.append(i)
        
        return res