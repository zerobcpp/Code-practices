class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = set()
        for i in range(len(nums)):
            if nums[i] in n:
                return True
            n.add(nums[i])
            
            if i - k >= 0:
                n.remove(nums[i-k])
        
        return False