class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        st = []
        s = list(s)
        for i in range(n):
            c = s[i]
            if c == '(':
                st.append(i)
            elif c == ')':
                if not st:
                    s[i] = ''
                else:
                    st.pop()
        
        while st:
            s[st.pop()] = ''
        
        return ''.join(s)