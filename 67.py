class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        newstring = []

        # fix string to identical length
        lenb = len(b)
        lena = len(a)
        if len(a) > len(b):
            while lenb < len(a):
                b = "0" + b
                lenb += 1
            else:
                while lena < len(b):
                    a = "0" + a
                    lena += 1

        carry = 0
        bit = 0
        #print(a)
        #print(b)

        i = len(a)-1
        while i >= 0:
            bit = carry
            bit += int(a[i])
            bit += int(b[i])

            newstring.append(bit%2)
            carry = bit//2
            i -= 1
        if carry != 0:
            newstring.append(carry)

        s = ""
        for i in newstring[::-1]:
            s += str(i)

        return s
