class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        
        for i in s:
            if i == '*':
                if st:
                    st.pop()
            else:
                st.append(i)
        
        #print(st)
        return ''.join(st)