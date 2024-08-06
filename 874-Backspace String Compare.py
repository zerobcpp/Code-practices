class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sst = []
        tst = []
        
        for i in s:
            if i == '#':
                if sst:
                    sst.pop()
            else:
                sst.append(i)
        
        for i in t:
            if i =='#':
                if tst:
                    tst.pop()
            else:
                tst.append(i)
        
        return tst == sst
    
    
    def backSpaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1
        
        ss = st = ''
            
        while i >= 0 or j >= 0:
            
            if i >= 0 and s[i] == '#':
                i -= 1
            if j >= 0 and s[j] == '#':
                j -= 1
                
            if j < 0:
                st = ''
            else:
                st = t[j]
            if i < 0:
                ss = ''
            else:
                ss = t[i]
                
            if ss != st:
                return False
        
        
        return True
                
        