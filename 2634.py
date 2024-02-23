class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        l, r = 0, 10 ** 9
        res = 10 ** 9
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid in nums1 and mid in nums2:
                res = min(res, mid)
            r = mid - 1
            
        
        return res