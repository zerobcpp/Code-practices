class Solution:
    def intToRoman(self, num: int) -> str:
        maps = [['M',1000], ['CM', 900], ['D',500], ['CD', 400], ['C',100], ['XC', 90],['L',50], ['XL', 40], ['X',10], ['IX', 9], ['V',5], ['IV',4], ['I',1]]
        n = len(maps)
        res = []
        for i in range(n):
            sym, val = maps[i]
            while num >= val:
                num -= val
                res.append(sym)
        
        #print(res)
        return ''.join(res)
        
                