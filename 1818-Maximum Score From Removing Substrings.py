class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        st = []
        
        for i in s:
            st.append(i)
            if x > y:
                while len(st) >= 2 and st[-1] == 'b' and st[-2] == 'a':
                    res += x
                    st.pop()
                    st.pop()
            else:
                while len(st) >= 2 and st[-1] == 'a' and st[-2] == 'b':
                    res += y
                    st.pop()
                    st.pop()
            #print(st, res)
                
            
        lower = []
        for i in st:
            lower.append(i)
            while len(lower) >= 2 and lower[-1] == 'b' and lower[-2] == 'a':
                res += x
                lower.pop()
                lower.pop()
            while len(lower) >= 2 and lower[-1] == 'a' and lower[-2] == 'b':
                res += y
                lower.pop()
                lower.pop()
        
        #print(res)
            
        return res
    
    def maximumGain(self, s, x, y):
        pairs = [(x, 'ab'), (y, 'ba')]
        pairs.sort(reverse = True)
        res = 0
        
        for pts, seq in pairs:
            st = []
            for i in s:
                if st and st[-1] == seq[0] and i == seq[1]:
                    st.pop()
                    res += pts
                else:
                    st.append(i)
            
            s = ''.join(st)
        
        return res
            
        
        