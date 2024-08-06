class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        st = []
        
        for i in logs:
            if i == '../':
                if st:
                    st.pop()
                
            elif i == './':
                continue
            else:
                st.append(i)
        
        #print(st)
        
        return len(st)
    
    
    def minOperations(self, logs):
        res = 0
        for i in logs:
            if i == '../':
                res -= 1
                res = max(res, 0)
            elif i == './':
                continue
            else:
                res += 1
        
        return res