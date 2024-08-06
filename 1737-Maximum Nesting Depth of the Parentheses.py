class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        st = []
        
        for i in s:
            if i == '(':
                st.append(i)
            elif i == ')':
                st.pop()
            
            res = max(res, len(st))
        
        return res