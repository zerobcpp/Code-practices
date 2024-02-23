class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        
        for i in range(n):
            head = manager[i]
            g[head].append(i)
        
        res = 0
        st = [headID]
        seen = set()
        while st:
            cur = st.pop()
            res += informTime[cur]
            for neigh in g[cur]:
                if neigh not in seen:
                    seen.add(neigh)
                    st.append(neigh)
        
        return res
        