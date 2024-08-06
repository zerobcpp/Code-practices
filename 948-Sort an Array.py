class Solution:
    def sortArrayQsort(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            pidx = randint(l,r)
            pivot, p = nums[pidx], l
            nums[r], nums[pidx] = nums[pidx], nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            return p
        
        def qSort(l, r):
            if l < r:
                pivot = partition(l,r)
                qSort(l, pivot-1)
                qSort(pivot+1, r)

        qs = set(nums)
        if len(qs) == 1:
            return nums
        qSort(0, len(nums)-1)
        return nums
    
    def sortArray(self, nums):
        heapify(nums)
        res = []
        while nums:
            res.append(heappop(nums))
        
        return res