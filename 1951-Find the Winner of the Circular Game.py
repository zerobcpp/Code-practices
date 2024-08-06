class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        st = deque(range(1, n+1))
        cnt = 1
        
        while len(st) > 1:
            if cnt == k:
                st.popleft()
                cnt = 0
            else:
                st.append(st.popleft())
            cnt += 1
            #print(st)
        
        return st[0]
    
    
    
    def findTheWinner(self, n, k):
        @cache
        def helper(n):
            if n <= 1:
                return 0
            
            return (helper(n-1) + k) % n 
        
        return helper(n) + 1