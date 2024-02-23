class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for u, v in sorted(tickets, reverse = True):
            graph[u].append(v)
        
        print(graph)
        res = []
        start = ['JFK']
        
        while start:

            
            
            while graph[start[-1]]:
                start.append(graph[start[-1]].pop())
            res.append(start.pop())
        return res[::-1]