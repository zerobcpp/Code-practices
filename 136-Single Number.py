class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # With extra memory:
        
        intkey = {}
        for i in nums:
            intkey[i] = intkey.get(i, 0) + 1
        
        for i, v in intkey.items(): 
            if intkey[i] == 1:
                return i