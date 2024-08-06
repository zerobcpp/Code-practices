class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digitcounter = 0
        evendigit = 0
        for i in nums:
            while i >= 1:
                i /= 10
                digitcounter += 1
            if digitcounter % 2 == 0:
                evendigit += 1
            digitcounter = 0
            
        return evendigit
                