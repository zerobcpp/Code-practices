class Solution:
    def average(self, salary: List[int]) -> float:
        mi = min(salary)
        ma = max(salary)
        N = len(salary)
        x = reduce(lambda x, y: x + y, salary)
        
        return (x-mi-ma) / (N-2)
    def average(self, salary):
        mi = min(salary)
        ma = max(salary)
        res = 0
        cnt = 0
        for i in salary:
            if i == mi or i == ma:
                continue
            res += i
            cnt += 1

        return res/cnt
    
    def average(self, salary):
        mi = 10 ** 6
        ma = 1000
        res = 0
        N = len(salary)
        for i in salary:
            mi = min(mi, i)
            ma = max(ma, i)
            res += i
        
        return (res - ma - mi) / (N - 2)