class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        if N == k:
            return '0'
        st = [] 
        i = 0
        
        while i < N:
            while k and st and st[-1] > num[i]:
                st.pop()
                k -= 1
            st.append(num[i])
            i += 1
        
        while k:
            st.pop()
            k -= 1
        
        st = st[::-1]
        while len(st) > 1 and st[-1] == '0':
            st.pop()
        
        return ''.join(st[::-1])