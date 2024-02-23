class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair = len(cost)
        res = [0] * stair
        res[0], res[1] = cost[0], cost[1]
        
        for i in range(2, stair):
            res[i] = cost[i] + min(res[i-1], res[i-2])
        #print(res)
        
        return res[-2] if res[-2] < res [-1] else res[-1]