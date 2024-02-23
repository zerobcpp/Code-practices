class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1).intersection(set(nums2))
        
        for i in nums2:
            if i in nums1:
                return i
        
        return -1
    
    
    def getCommon(self, n1, n2):
        p1, p2 = 0, 0
        n, m = len(n1), len(n2)
        
        while p1 < n and p2 < m:
            if n1[p1] == n2[p2]:
                return n1[p1]
            if n1[p1] > n2[p2]:
                p2 += 1
            else:
                p1 += 1
        return -1
    
    def getCommon(self, n1, n2):
        c = Counter(n1)
        
        for i in n2:
            if c[i] >= 1:
                return i
        
        return -1