class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        print(events)
        N = len(events)
        cache = {}
        def helper(idx, start, count):
            
            if idx >= N or count <= 0: 
                return 0
            if start >= events[idx][0]:
                return helper(idx+1, start, count)
            if (count, idx) in cache:
                return cache[count, idx]
            
            res = max(helper(idx+1, start, count), \
                      helper(idx+1, events[idx][1], count - 1) + events[idx][2])
            
            cache[count, idx] = res
            
            return res
        helper(0, 0, k)
        return cache[k, 0]