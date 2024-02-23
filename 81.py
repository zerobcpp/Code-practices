class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid] >= nums[l]:
                #if target >= nums[l] and target < nums[mid]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                #if target > nums[mid] and target <= nums[r]:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
                