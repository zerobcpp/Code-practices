class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        res = 0
        op = '*+-/'
        for i in tokens:
            if i in op:
                y = st.pop()
                x = st.pop()
                cur = 0
                if i == '+':
                    cur += (x + y)
                elif i == '-':
                    cur += (x - y)
                elif i == '*':
                    cur += (x * y)
                else:
                    cur += int((x / y))
                st.append(cur)
            else:
                st.append(int(i))
        
        return st[0]
        
            
            