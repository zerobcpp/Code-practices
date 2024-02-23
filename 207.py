class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = [0 for i in range(numCourses)]
        neighbor = [[] for i in range(numCourses)]
        for cur, pre in prerequisites:
            course[cur] += 1
            neighbor[pre].append(cur)
        
        stack = [i for i in range(numCourses) if i == 0]
        res = []
        while stack:
            start = stack.pop()
            res.append(start)
            for n in neighbor[start]:
                course[n] -= 1
                if not course[n]:
                    stack.append(n)
        
        return len(res) == numCourses