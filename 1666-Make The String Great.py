class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        
        for i in s:
            st.append(i)
            
            while len(st) > 1 and abs(ord(st[-1]) - ord(st[-2])) == 32:
                st.pop()
                st.pop()
            

        
        return ''.join(st)