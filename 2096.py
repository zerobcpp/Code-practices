class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res = [1] * n
        
    
        ret = []
    
        for i, v in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect_right(ret, v)
            
            if idx == len(ret):
                ret.append(v)
            else:
                ret[idx] = v
            res[i] = idx + 1
            
        return res