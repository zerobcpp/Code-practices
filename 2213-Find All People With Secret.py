class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        
        for u, v, t in meetings:
            graph[u].append((t, v))
            graph[v].append((t, u))
            
        st = []
        heappush(st, (0, 0))
        heappush(st, (0, firstPerson))
        seen = set()
        while st:
            t, sp = heappop(st)
            if sp in seen:
                continue
            seen.add(sp)
            
            for time, neigh in graph[sp]:
                if time >= t and neigh not in seen:
                    heappush(st, (time, neigh))
                    #seen.add((neigh))
        
        return seen
    
        
        '''
        st = [(0, 0, firstPerson)]
        graph = defaultdict(list)
        for u, v, t in meetings:
            graph[u].append((v, t))
            
        print(graph)
        while st:
            time, sp, pp = heappop(st)
        
        return res
        
        """
        meetings.sort(key = lambda x: x[2])
        meetings.append([-1, -1, 10 ** 6])
        graph = defaultdict(list)
        
        #print(meetings)
        secret = set([0, firstPerson])
        
        st = [(0, 0, firstPerson)]
        
        for u, v, t in meetings:
            while st and t > st[0][0]:
                cur = heappop(st)
                # t, u, v
                if cur[1] in secret or cur[2] in secret:
                    graph[cur[1]].append(cur[2])
                    graph[cur[2]].append(cur[1])
                    secret.add(cur[1])
                    secret.add(cur[2])
            heappush(st, (t, u, v))
            
            
        #print(graph, st)
        st = [0]
        seen = set([0])
        while st:
            cur = st.pop()
            for neigh in graph[cur]:
                if neigh not in seen:
                    st.append(neigh)
                    seen.add(neigh)
                    
        return list(seen) 
        '''
        
        