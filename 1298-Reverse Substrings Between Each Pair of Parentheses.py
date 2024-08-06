class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        
        for i in s:
            if i == ')':
                temp = []
                while st and st[-1] != '(':
                    temp.append(st.pop())
                #print(temp, st)
                st.pop()
                st.extend(temp)
            else:
                st.append(i)
        
        
        return ''.join(st)