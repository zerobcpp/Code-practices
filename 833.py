class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        
        for r in routes:
            n = len(r)
            for i in range(1, n):
                graph[r[i-1]].append(r[i])
                graph[r[i]].append(r[i-1])
            graph[r[n-1]].append(r[0])
            
        
        def helper(node):
            cnt = 0
            st = [node]
            seen = set(st)
            while st:
                cur = st.pop()
                #print(cur, end = '->')
                
                for neigh in graph[cur]:
                    if neigh == target:
                        return cnt
                    if neigh not in seen:
                        st.append(neigh)
                        seen.add(neigh)
                cnt += 1
            return float('inf')

        
        res = helper(source)
        return res if res != float('inf') else -1
        