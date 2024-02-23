class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        outcome = dict()
        
        for (u, v) , q in zip(equations, values):
            graph[u].append(v)
            graph[v].append(u)
            outcome[f'{u}/{v}'] = q
            outcome[f'{v}/{u}'] = 1/q
        
        res = []
        
        for n, d in queries:
            if n not in graph or d not in graph:
                res.append(-1.0)
            else:
                seen = set()
                seen.add(n)
                st = [(n, 1)]
                while st:
                    cur, val = st.pop()
                    if cur == d:
                        res.append(val)
                        break
                    for neigh in graph[cur]:
                        if neigh not in seen:
                            temp = outcome[f'{cur}/{neigh}']
                            st.append((neigh, val * temp))
                            seen.add(neigh)
        
        return res
                        