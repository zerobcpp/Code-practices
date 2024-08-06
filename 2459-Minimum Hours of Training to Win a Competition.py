class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ep, exp = initialEnergy, initialExperience
        sumep = sum(energy) + 1
        rest = 0 if sumep - ep < 0 else sumep-ep
        n = len(experience)
        
        for i in experience:
            while exp <= i:
                rest += 1
                exp += 1
            exp += i
        return rest