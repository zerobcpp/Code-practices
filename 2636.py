class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        N = len(nums1)
        def helper(arr, arr2, n, idx):
            nonlocal res
            #print(arr, arr2, n)
            if n == 0:
                res = max(res, sum(arr) * min(arr2))
                return 
            if idx >= N:
                return 
            helper(arr+[nums1[idx]], arr2+[nums2[idx]], n-1, idx+1)
            helper(arr, arr2, n, idx+1)
        
        helper([], [], k, 0)
        #print(res)
        return res