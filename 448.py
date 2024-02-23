class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nots = []
        n = len(nums)
        for i in range(1, n+1):
            if i not in nums:
                nots.append(i)
        
        return nots