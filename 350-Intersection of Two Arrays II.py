class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        print(list(c1.elements()))
        return list((c1&c2).elements())
    
    
    
    def intersect(self, n1, n2):
        c1 = {}
        c2 = {}
        for i in n1:
            c1[i] = c1.get(i, 0) + 1
        
        for i in n2:
            c2[i] = c2.get(i, 0) + 1
        
        res = []
        
        for i, v in c1.items():
            if i in c2:
                f = min(v, c2[i])
                while f:
                    res.append(i)
                    f -= 1
        
        return res