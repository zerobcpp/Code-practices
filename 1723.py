class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        graph = [0] * N
        self.ret = 0
        def helper(i, c):
            if i >= N:
                for i in range(N):
                    if graph[i] != 0:
                        return
                self.ret = max(self.ret, c)
                return
            u, v = requests[i][0], requests[i][1]
            graph[u] -= 1
            graph[v] += 1
            helper(i+1, c+1)
            graph[u] += 1
            graph[v] -= 1
            helper(i+1, c)
            
        helper(0, 0)
        return self.ret
                    