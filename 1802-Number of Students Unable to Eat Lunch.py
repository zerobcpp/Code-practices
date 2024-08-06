class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while True:
            serve = False
            n = len(students)
            for _ in range(n):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                    serve = True
                else:
                    students.append(students.popleft())
            if not serve:
                break
                
        return len(students)