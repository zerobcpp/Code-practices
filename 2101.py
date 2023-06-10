# 2101. Detonate the Maximum Bombs

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        ret = 0
        graph = {i: [] for i in range(N)}
        
        for i in range(N):
            x, y, d = bombs[i]
            for j in range(N):
                if i == j:
                    continue
                cx, cy, cd = bombs[j]
                if d ** 2 >= (cx - x) ** 2 + (cy - y) ** 2:
                    graph[i].append(j)
        ret = 0
        def helper(idx):
            nonlocal ret
            st = [idx]
            seen = set(st)
            res = 0
            while st:
                cur = st.pop()
                res += 1
                for neigh in graph[cur]:
                    if neigh not in seen:
                        seen.add(neigh)
                        st.append(neigh)
            
            ret = max(ret, res)
            return
        
        visit = set()
        for i in range(N):
            if i not in visit:
                visit.add(i)
                helper(i)
        
        return ret