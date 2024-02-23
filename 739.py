class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0 for i in temp]
        for i in range(len(temp)):
            count = 0
            for j in range(i+1, len(temp)):
                if temp[j] > temp[i]:
                    res[i] = j - i
                    break
        
        return res