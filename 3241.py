class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        
        l = 0
        res = []
        while l < N:
            temp = []
            r = l
            safe = True
            
            while r < l + 3 and r < N:
                if nums[r] - nums[l] > k:
                    safe = False
                    break
                temp.append(nums[r])
                r += 1
            
            if safe:
                res.append(temp)
            else:
                return []
            l += 3
        
        #print(res)
        
        return res
    
    
    def divideArray(self, nums, k):
        nums.sort()
        l = 0
        N = len(nums)
        res = []
        
        while l < N:
            safe = True
            
            if nums[l+2] - nums[l] > k:
                safe = False
            
            if safe:
                res.append([nums[l], nums[l+1], nums[l+2]])
            else:
                return []
            l += 3
        
        return res