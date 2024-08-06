class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        job = sorted(zip(startTime, endTime, profit))
        print(job)
                
        @cache
        def helper(i):
            if i >= N:
                return 0
            
            p = 0
            j = bisect_left(job, (job[i][1], ))
            #print(j)
            p = job[i][2] + helper(j)
            ntake = helper(i+1)
            
            return max(p, ntake)

#         @cache
#         def helper(i):
#             if i >= N:
#                 return 0
            
            
#             p = 0
#             ntake = helper(i+1)
#             k = None
#             for j in range(i+1, N):
#                 if job[j][0] >= job[i][1]:
#                     k = j
#                     break
                    
#             p = job[i][2] + (helper(k) if k != None else 0)
#             return max(p, ntake)
        
        return helper(0)
    
    def jobScheduling(self, start, end, profit):
        INF = 10 ** 9 + 1
        N = len(start)
        job = sorted(zip(start, end, profit))
        job.append((INF, INF, 0))
        #print(job)
        res = 0
        cur = 0
        st = []
        for s, e, p in job:
            
            while st and st[0][0] <= s:
                cur = max(cur, st[0][1])
                heappop(st)
            
            heapq.heappush(st, (e, p + cur))
            #print(st, cur)
        
        return cur
        