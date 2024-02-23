class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        @cache
        def helper(idx, cd):
            if idx >= N:
                return 0
            count = 0
            pts, bp = questions[idx]
            count = 0
            #print(idx, cd)
            if cd == 0:
                count = max(pts + helper(idx+1, cd + bp), helper(idx +1, cd))
            else:
                count = helper(idx+1, cd-1)
            return count
        
        return helper(0, 0)
            