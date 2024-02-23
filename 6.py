class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strs = [[] for i in range(numRows)]
        alt = False
        count = 0
        for i in s:
            if count == numRows - 1 or count == 0:
                alt = not alt
            strs[count].append(i)
            if alt:
                count += 1
            else:
                count -= 1
            
        res = []
        for i in strs:
            res += i
        
        return ''.join(res)
            
            