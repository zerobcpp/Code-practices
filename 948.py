class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            low, high = l, r
            pivot = nums[l]
            low += 1
            while low <= high:
                if pivot >= nums[low]:
                    low += 1
                if pivot < nums[r]:
                    high -= 1
                if low < high:
                    nums[low], nums[high] = nums[high], nums[low]
            nums[l], nums[high] = nums[high],nums[l]
            #print(nums)
            return high 
            
            
        
        def qSort(l,  r):
            if l < r:
                pivot = partition(l, r)
                qSort(l, pivot - 1)
                qSort(pivot + 1, r)
            
        
        qSort(0, len(nums)-1)
        return nums
            