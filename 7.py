class Solution(object):
    def reverse(self, x):
        intToString = str(x)
        if x < 0:
            reversedInt = int('-' + intToString.replace('-', ' ')[::-1])
        else:
            reversedInt = int(intToString[::-1])

        if abs(reversedInt) < 2 ** 31 and reversedInt > -2 ** 31 - 1:
            return reversedInt
        else:
            return 0