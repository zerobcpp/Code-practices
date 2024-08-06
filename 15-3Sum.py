class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if (sorted([nums[i],nums[j],nums[k]])) in res:
                            continue
                        res.append(sorted([nums[i],nums[j], nums[k]]))
        return res
                    
        
    
    def threeSum(self, nums):
        nums.sort()
        res = set()
        N = len(nums)
        
        for i in range(N):
            l = i + 1
            r = N - 1
            
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    res.add((nums[i], nums[l], nums[r]))
                
                if cur > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
    
    
    def threeSum(self, nums):
        N = len(nums)
        res = set()
        dups = set()
        for i in range(N):
            c = {}
            if nums[i] not in dups:
                for j in range(i+1, N):
                    cur = -nums[i] - nums[j]
                    if cur in c:
                        res.add(tuple(sorted((nums[i], nums[j], cur))))
                        
                    #print(nums[i], nums[j], cur, c)
                    c[nums[j]] = i
            dups.add(nums[i])
                
                
        
        return res
                