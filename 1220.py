class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         c = Counter(req_skills)
#         N = len(people)
#         res = []
#         def helper(i, cur):
#             if i >= N:
#                 return float('inf')
            
#             if all(cur[i] == 0 for i in cur):
#                 return 0
            
#             count = nc = float('inf')
            
#             nc = helper(i+1, cur)
#             req = False
#             for skill in people[i]:
#                 if skill in cur and cur[skill] > 0:
#                     cur[skill] -= 1
#                     req = True
#                 if req:
#                     count = 1 + helper(i+1, cur)

            
            
#             return min(count, nc)
           
            
        
#         return helper(0, c)
                
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(n):
                new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)
                    if (dp[skills_mask] == -1 or
                        people_mask.bit_count()
                       < dp[skills_mask].bit_count()):
                        dp[skills_mask] = people_mask
            return dp[skills_mask]
        answer_mask = f((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans
        