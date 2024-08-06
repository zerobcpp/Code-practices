class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        graph = defaultdict(list)
        val = {}
        
        for (n, d), q in zip(equations, values):
            graph[n].append(d)
            graph[d].append(n)
            val[n, d] = q
            val[d, n] = 1/q
        
        for s, e in queries:
            if s not in graph or e not in graph:
                res.append(-1.0)
            else:
                seen = set()
                goal = False
                st = [(s, 1)]

                while st:
                    cur, temp = st.pop()
                    if cur == e:
                        res.append(temp)
                        goal = True
                        break
                    for neigh in graph[cur]:
                        if neigh not in seen:
                            prod = val.get((cur, neigh), 0) * temp
                            st.append((neigh, prod))
                            seen.add(neigh)
                if not goal:
                    res.append(-1.0)

        
        return res
                        