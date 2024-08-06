class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(students)
        res = 0
        for i in range(n):
            res += abs(students[i] - seats[i])
        
        return res