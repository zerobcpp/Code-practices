class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        graph = {i: [] for i in range(numCourses)}
        degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            degree[u] += 1
        stack = [i for i, v in enumerate(degree) if not v]
        while stack:
            cur = stack.pop()
            res.append(cur)
            for n in graph[cur]:
                degree[n] -= 1
                if not degree[n]:
                    stack.append(n)

        # print(degree)
        return len(res) == numCourses

    def canFinish(self, numCourses, pre):
        graph = {i: [] for i in range(numCourses)}
        for u, v in pre:
            graph[v].append(u)

        # can change seen into number array, this is a container to store what currently processing.
        # if the node is currently in the processing window, it means that you have a cycle.
        seen = set()
        def helper(n):
            if n in seen:
                return False
            if graph[n] == []:
                return True
            seen.add(n)
            for neigh in graph[n]:
                if not helper(neigh):
                    return False
            seen.remove(n)
            graph[n] = []
            return True

        for i in range(numCourses):
            if not helper(i):
                return False

        return True