class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        left = 0
        right = 0
        for i in range(n):
            if s[i] in '(*': 
                left += 1
            else:
                left -= 1
            
            if left < 0:
                return False
        
        if left < 0:
            return False
        for i in range(n-1, -1, -1):
            if s[i] in ')*':
                right += 1
            else:
                right -= 1
            
            if right < 0:
                return False
        
        if right < 0:
            return False
        return True
    
    
    def checkValidString(self, s):
        lmn = 0
        lmx = 0
        
        for i in s:
            if i == '(':
                lmx += 1
                lmn += 1
            elif i == ')':
                lmx -= 1
                lmn -= 1
            else:
                lmx += 1
                lmn -= 1
            
            if lmx < 0:
                return False
            lmn = max(0, lmn)
        #print(lmx, lmn)
        return lmn == 0