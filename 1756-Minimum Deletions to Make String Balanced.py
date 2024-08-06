class Solution:
    def minimumDeletions(self, s: str) -> int:
        st = []
        res = 0
        for i in s:
            if st and i == 'a' and st[-1] == 'b':
                res += 1
                st.pop()
            else:
                st.append(i)
        
        return res