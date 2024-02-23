class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = {i : [] for i in range(n)}
        
        for i in range(n):
            head = manager[i]
            if head != -1:
                g[head].append(i)
        
        res = 0
        st = [(headID, informTime[headID])]
        while st:
            cur, time = st.pop()
            res = max(res, time)
            for neigh in g[cur]:
                st.append((neigh, time + informTime[neigh]))
        
        return res
        