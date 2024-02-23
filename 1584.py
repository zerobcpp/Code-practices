class Solution:
    def average(self, salary: List[int]) -> float:
        mi = min(salary)
        ma = max(salary)
        N = len(salary)
        x = reduce(lambda x, y: x + y, salary)
        
        return (x-mi-ma) / (N-2)
    
