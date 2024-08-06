import numpy as np
class Solution:
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = -np.inf
        for i in nums:
            if i > one:
                one, two, three = i, one, two
            elif i > two and i < one:
                two, three = i, two
            elif i > three and i < two:
                three = i
        return three if three != -np.inf else one