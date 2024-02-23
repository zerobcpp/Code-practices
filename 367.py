class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lt, rt =  0, num
        
        while lt <= rt:
            mid = lt + (rt - lt) //2
            if mid**2 == num:
                return True
            if mid ** 2 > num:
                rt = mid - 1
            else:
                lt = mid + 1
        return False