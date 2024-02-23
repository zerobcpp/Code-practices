class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counters = []
        cnt = 0 
        anw = 0 
        for i in nums:
            if i == 1:
                cnt += 1
                anw = max(cnt,anw)
            else:
                cnt = 0
        
        return anw