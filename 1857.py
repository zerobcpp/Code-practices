class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        g = {i: [] for i in range(n)}
        node = {}
        degree = [0] * n
        for u, v in edges:
            g[u].append(v)
            degree[v] += 1
        i = 0
        for c in colors:
            node[i] = c
            i += 1

        st = [i for i in range(n) if not degree[i]]
        c = []
        cnt = defaultdict(lambda: defaultdict(int))
        res = 0
        while st:
            cur = st.pop()
            c.append(cur)
            cnt[cur][node[cur]] += 1
            res = max(res, cnt[cur][node[cur]])
            for neigh in g[cur]:
                for idx in cnt[cur]:
                    cnt[neigh][idx] = max(cnt[neigh][idx], cnt[cur][idx])
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    st.append(neigh)

        print(cnt)
        return res if n == len(c) else - 1