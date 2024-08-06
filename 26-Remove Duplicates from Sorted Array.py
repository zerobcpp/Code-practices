class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        k = len(set(nums))
        while i < n:
            
            
            runner = swap = i + 1
            count = 1
            while runner < n and (nums[i] == nums[runner] or nums[runner] == ''):
                nums[runner] = ''
                runner += 1
                count += 1
            
            if count > 1 and runner < n:
                nums[swap] = nums[runner]
                
            i += 1
            
            
        print(nums, k)
        return k