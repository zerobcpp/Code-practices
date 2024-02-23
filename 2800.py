class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for i in s:
            st.append(i)
            if len(st) >= 2:
                if (st[-2] == 'A' and st[-1] == 'B') or (st[-2] =='C' and st[-1] == 'D') :
                    st.pop()
                    st.pop()
            
        #print(st)
        return len(st)