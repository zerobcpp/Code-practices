class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [0 for i in range(n)]
        for i, o in edges:
            adj[o] += 1
        res = []
        for i in range(n):
            if adj[i] == 0:
                res.append(i)
        
        return res
    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        seen = set()
        for i, o in edges:
            graph[i].append(o)
        
        def helper(node):
            seen.add(node)
            st = [node]
            while st:
                cur = st.pop()
                for neigh in graph[cur]:
                    if neigh not in seen:
                        st.append(neigh)
                        seen.add(neigh)
                    elif neigh in res:
                        res.remove(neigh)
        res = set()
        for i in range(n):
            if i not in seen:
                res.add(i)
                helper(i)
        
        return res