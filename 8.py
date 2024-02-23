class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = ""

        negative = False
        for i in s:
            if i == ' ':
                continue
            elif i == '-':
                negative = True
            elif not i.isdigit():
                continue
            else:
                c += i
        if negative:
            c = -int(c)

        if int(c) >= 2**31-1:
            return 2**31-1
        elif int(c) <= -2**31 and negative:
            return -2**31
        elif c == '':
            return 0
        else:
            return c