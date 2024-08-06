class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        res = 0
        for i in nums:
            diff = k - i
            if c[diff] > 0:
                c[diff] -= 1
                res += 1
            else:
                c[i] += 1
            #print(c)
        
        return res
    
    def maxOperations(self, nums, k):
        c = {}
        res = 0
        for i in nums:
            diff = k - i
            if diff in c and c[diff] > 0:
                c[diff] -= 1
                res += 1
            else:
                c[i] = c.get(i, 0) + 1
        
        return res
    
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            print(l, r)
            if nums[l] + nums[r] == k:
                res += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        
        return res