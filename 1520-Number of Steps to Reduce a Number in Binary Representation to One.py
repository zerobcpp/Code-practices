class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        res = 0
        while ''.join(s) != '1':
            n = len(s)
            if s[n-1] == '0':
                s = s[:n-1]
            else:
                carry = False
                for i in range(n-1, -1, -1):
                    if s[i] == '1':
                        s[i] = '0'
                    else:
                        carry = True
                        s[i] = '1'
                        break
                    
                if not carry:
                    s = ['1'] + s
            res += 1
            
            #print(s)
        
        return res
                    
                    
                
                
                

"""
1101 -> 1110  -> 0111 -> 1000 -> 0010 -> 0010 -> 0001
"""