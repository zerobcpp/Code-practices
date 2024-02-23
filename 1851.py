class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        #print(events)
        N = len(events)
        #cache = {}
        cache = [[-1] * (k+1) for _ in range(N)]

        def helper(idx, start, count):
            
            if idx >= N or count <= 0: 
                return 0
            if start >= events[idx][0]:
                return helper(idx+1, start, count)
#             if (count, idx) in cache:
#                 return cache[count, idx]

            if cache[idx][count] != -1:
                return cache[idx][count]
        
            res = max(helper(idx+1, start, count), \
                      helper(idx+1, events[idx][1], count - 1) + events[idx][2])
            
            cache[idx][count] = res
            
            return res
        helper(0, 0, k)
        return cache[0][k]