class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)[::-1]
        b = ""
        negative = False
        for i in a:
            if i == "-":
                negative = True
            elif i == "0":
                continue
            else:
                b += i

        if negative:
            return -int(b)
        return int(b)