# 399. Evaluate Division

class Solution:
    def calcEquationDFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        outcome = dict()

        for (u, v), q in zip(equations, values):
            graph[u].append(v)
            graph[v].append(u)
            outcome[u, v] = q
            outcome[v, u] = 1 / q

        res = []

        for n, d in queries:
            if n not in graph or d not in graph:
                res.append(-1.0)
            else:
                seen = set()
                seen.add(n)
                st = [(n, 1)]
                goal = False
                while st:
                    cur, val = st.pop()
                    if cur == d:
                        res.append(val)
                        goal = True
                        break
                    for neigh in graph[cur]:
                        if neigh not in seen:
                            temp = outcome[cur, neigh]
                            st.append((neigh, val * temp))
                            seen.add(neigh)
                if not goal:
                    res.append(-1.0)
        return res

    def calcEquationDSU(self, equ, val, query):
        uf = DSU()
        for (u, v), q in zip(equ, val):
            uf.union(u, v, q)
        res = []
        # print(uf.outcome)
        for x, y in query:
            if x not in uf.parent or y not in uf.parent or uf.find(x)[0] != uf.find(y)[0]:
                res.append(-1.0)
            else:
                if (x, y) in uf.outcome:
                    res.append(uf.outcome[x, y])
                else:
                    xp, xv = (uf.find(x))
                    yp, yv = (uf.find(y))
                    temp = yv / xv
                    uf.outcome[xp, yp] = temp
                    res.append(temp)

        return res


class DSU:
    def __init__(self):
        self.parent = defaultdict(str)
        self.rank = defaultdict(int)
        self.outcome = defaultdict(lambda: 1)

    def find(self, x, temp=1):
        if x not in self.parent:
            self.parent[x] = x
        while x != self.parent[x]:
            temp *= self.outcome[self.parent[x], x]
            x = self.parent[x]
        return (x, temp)

    def union(self, x, y, q):
        self.outcome[x, y] = q
        self.outcome[y, x] = 1 / q
        (xp, xv), (yp, yv) = self.find(x), self.find(y)

        if xp == yp:
            return

        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp] += 1

        qq = q * xv / yv
        self.outcome[xp, yp] = qq
        self.outcome[yp, xp] = 1 / qq






