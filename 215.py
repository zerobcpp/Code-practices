class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
        
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        def helper(l, r):
            pidx = randint(l,r)
            p, pivot = l, nums[pidx],
            nums[r], nums[pidx] = nums[pidx], nums[r]
            
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return helper(0, p-1)
            elif p < k:
                return helper(p+1, r)
            else:
                return nums[p]
        
        return helper(0, len(nums)-1)

