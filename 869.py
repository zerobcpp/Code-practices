class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        seen = set()
        def check(s1, s2):
            n = len(s1)
            cnt = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    cnt += 1
            
            return cnt == 1 or cnt == 2
        def helper(node):
            st = [node]
            seen.add(node)
            while st:
                cur = st.pop()
                seen.add(cur)
                for neigh in graph[cur]:
                    if neigh not in seen:
                        st.append(neigh)
                        
            return
                    
        graph = {i : [] for i in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                if check(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        
        #print(graph)
        res = 0
        for i in range(N):
            if i not in seen:
                helper(i)
                print(seen, i)
                res += 1
        
        return res 
            
        
        
        