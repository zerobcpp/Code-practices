class Solution:
    def romanToInt(self, string: str) -> int:
        parse = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        sum = 0
        for i in range(0, len(string)-1):
            l = string[i]
            r = string[i+1]
            if parse[l]<parse[r]:
                sum -= parse[l]
            else:
                sum += parse[l]

            #sum += parse[string[-1]]
        return sum + parse[string[-1]]
