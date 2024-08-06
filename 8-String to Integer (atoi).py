class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s.isdigit():
            res = int(s)
            if 2**31-1 >= res >= -2**31:
                return res
            else:
                return 2**31-1 if res > 2**31-1 else -2**31
        res = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i] in ' .' or (i!=0 and s[i] in '+-'):
                break
            else:
                res += s[i]
        if res:
            res = int(res) if res.isdigit() or res[1:].isdigit() else 0
            if 2**31-1 >= res >= -2**31:
                return res
            else:
                return 2**31-1 if res > 2**31-1 else -2**31
        return 0