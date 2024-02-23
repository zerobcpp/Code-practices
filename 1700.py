class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        st = []
        i = 0
        for color, cost in zip(colors, neededTime):
            ins = True
            #print(color, cost)
            while st and st[-1][0] == color:
                if cost > st[-1][1]:
                    res += st[-1][1]
                    st.pop()
                else:
                    
                    res += cost
                    ins = False
                    #print(st, color, cost, ins)
                    break
            
            if ins:
                st.append((color, cost))
            
        
        #print(st)
        return res
    
    def minCost(self, colors, nTime):
        res = 0
        n = len(colors)
        
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                time = min(nTime[i-1], nTime[i])
                nTime[i] = max(nTime[i], nTime[i-1])
                res += time
        
        return res
            