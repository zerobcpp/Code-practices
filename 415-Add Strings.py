class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sol = []
        l1, l2 = len(num1)-1, len(num2)-1
        carry = 0
        while l1 >= 0 or l2 >= 0 or carry:
            v1 = v2 = 0
            if l1 >= 0:
                v1 = ord(num1[l1]) - ord('0')
                l1 -= 1
            if l2 >= 0:
                v2 = ord(num2[l2]) - ord('0')
                l2 -= 1
            
            #x = v1 + v2 + carry
            carry, val = divmod(v1+v2+carry, 10)
            sol.append(val)
        
        return "".join(str(i) for i in sol[::-1])