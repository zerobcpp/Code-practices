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
            print(shift)
            for j in range(i+1):
                string[j] = chr(ord(string[j])+shift)
        return "".join(string)