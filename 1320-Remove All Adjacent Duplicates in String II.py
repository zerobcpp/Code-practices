class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        
        for i in s:
            if st and st[-1][0] == i:
                st[-1][1] += 1
            else:
                st.append([i,1])
            while st and st[-1][1] >= k:
                st.pop()

        
        res = []
        for f, v in st:
            res.append(v*f)
        
        return ''.join(res)