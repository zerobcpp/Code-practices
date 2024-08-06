class Solution(object):
    def canFinish(self, n, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = {i : [] for i in range(n)}
        adj = [0] * n
        for u, v in pre:
            g[v].append(u)
            adj[u] += 1
        
        st = [i for i in range(n) if not adj[i]]
        
        res = []
        while st:
            cur = st.pop()
            res.append(cur)
            
            for neigh in g[cur]:
                adj[neigh] -= 1
                if not adj[neigh]:
                    st.append(neigh)
        
        return len(res) == n
            