class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        upper = int(c ** 0.5) + 1
        
        for i in range(upper):
            for j in range(i+1, upper):
                if i*i + j*j == c:
                    return True
        return False