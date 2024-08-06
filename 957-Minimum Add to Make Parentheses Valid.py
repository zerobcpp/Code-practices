class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for i in s:
            if i == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        
        return len(st)
    
    
    def minAddToMakeValid(self, s):
        res = 0
        ans = 0
        for i in s:
            if i == ')':
                res -= 1
            else:
                res += 1
            
            if res < 0:
                ans += 1
                res = 0
        
        return ans + res
                