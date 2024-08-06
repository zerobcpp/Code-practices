class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        left = 0
        cur = []
        for i in pushed:
            while st and st[-1] == popped[left]:
                cur.append(st.pop())
                left += 1
            st.append(i)
            
        
        while st:
            cur.append(st.pop())
        
        
        return cur == popped
            