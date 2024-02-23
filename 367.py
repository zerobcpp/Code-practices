class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        arr = [i**2 for i in range(num//2)]
        lt, mid, rt = 0, 0, len(arr) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            #print(arr[mid])
            if arr[mid] == num:
                return True
            
            if arr[mid] < num:
                lt = mid + 1
            else:
                rt = mid - 1
        
        return False