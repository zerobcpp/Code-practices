#2542. Maximum Subsequence Score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        pair = list(zip(nums1, nums2))
        pair.sort(key = lambda x: x[1], reverse = True)
        #print(pair)
        
        arr1, arr2 = [], []
        tot = 0
        for i, j in pair:
            heappush(arr1, i)   
            tot += i
            if len(arr1) > k:
                tot -= heappop(arr1)
                
            if len(arr1) == k:
                res = max(res, tot * j)

        return res
            
            
        
        