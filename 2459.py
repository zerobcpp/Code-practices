class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ep, exp = initialEnergy, initialExperience
        sumep = sum(energy) + 1
        rest = sumep - ep
        #print(rest)
        n = len(experience)
        
        for i in range(0,n-1):
            if exp < experience[i]:
                rest += (experience[i] - exp + 1)
            exp += experience[i]
            
        return rest