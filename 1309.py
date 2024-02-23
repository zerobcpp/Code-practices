class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
                
        adj_item = [0] * n
        adj_group = [0] * (group_id)
        g_graph = {i:[] for i in range(group_id)}
        i_graph = {i:[] for i in range(n)}
        #print(group)
        for i in range(n):
            
            for b in beforeItems[i]:
                adj_item[i] += 1
                i_graph[b].append(i)
            
                if group[i] != group[b]:
                    g_graph[group[b]].append(group[i])
                    adj_group[group[i]] += 1
        
        #print(adj_item, i_graph)
        #print(adj_group, g_graph)
        
        def helper(graph, adj):
            n = len(adj)
            st = [i for i in range(n) if adj[i] == 0]
            res = []
            while st:
                cur = st.pop()
                res.append(cur)
                for neigh in graph[cur]:
                    adj[neigh] -= 1
                    if adj[neigh] == 0:
                        st.append(neigh)
            
            return res if len(res) == n else None
        
        
        item = helper(i_graph, adj_item)
        gp = helper(g_graph, adj_group)
        #print(item, gp)
        if not item or not gp:
            return []
        
        c = defaultdict(list)
        for i in item:
            key = group[i]
            c[key].append(i)
        
        res = []
        
        for g in gp:
            res += c[g]
        
        return res