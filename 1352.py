class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        job = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        #job.sort(lambda x: x[1])
        #print(job)
        @cache
        def helper(i, end):
            if i >= N:
                return 0
            
            
            p = 0
            ntake = helper(i+1, end)
            if job[i][0] >= end:
                p = helper(i+1, job[i][1]) + job[i][2]
            
            return max(p , ntake)
        
        return helper(0, 0)
        