class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # With extra memory:
        
        intkey = {}
        for i in range(max(nums)+1):
            intkey[i] = 0

        for i in nums:
            intkey[i] +=1
            
        for k, v in intkey.items():
            if v == 1:
                return k