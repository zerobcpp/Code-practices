class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        N = len(skill)
        l, r = 0, N - 1
        res = 0
        balance = []
        while l < r:
            res += skill[l] * skill[r]
            balance.append(skill[l] + skill[r])
            l += 1
            r -= 1
        
        for i in range(1, len(balance)):
            if balance[i] != balance[i-1]:
                return -1
        # print(res, balance)
        return res
            
        
            