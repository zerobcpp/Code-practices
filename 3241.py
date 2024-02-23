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
        
        print(res)
        
        return res