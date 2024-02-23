class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        N = len(obstacles)
        res = [1] * N
        track = []
        
        for i, v in enumerate(obstacles):
            idx = bisect_right(track, v)
            if idx == len(track):
                track.append(v)
            else:
                track[idx] = v
            
            res[i] = idx + 1
        
        return res