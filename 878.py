class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        string = list(s)
        for i in range(len(shifts)):
            shift = shifts[i]
            #print(shift)
            for j in range(i+1):
                # ascii 97 = a, 122 = z
                asc = ord(string[j]) + (shift%26)
                if asc > 122:
                    asc -= 26
                string[j] = chr(asc)
        return "".join(string)