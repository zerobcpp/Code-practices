class Solution:
    def bestClosingTime(self, cust: str) -> int:
        mx = mn = 0
        for i in cust:
            if i == 'Y':
                mx += 1
        
        mn = mx
        res = 0
        for i, v in enumerate(cust):
            
            if v == 'Y':
                mn -= 1
            else:
                mn += 1
                
            if mn < mx:
                #print('here')
                res = i
                mn = mx
        
        return res + 1