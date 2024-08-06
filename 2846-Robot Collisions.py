class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()
        #print(robots, '\n')

        def helper(cur, other):
            cpos, cdirs, cidx = cur
            opos, odirs, oidx = other
            
            if cpos < opos and odirs == 'L' and cdirs == 'R':
                return True
            if cpos > opos and odirs == 'R' and cdirs == 'L':
                return True
            
            return False
                
            
            
        st = []
        
        for i in robots:
            pos, hp, dirs, idx = i
            #print(pos, hp, dirs, idx, n)
            while st and helper((st[-1][0], st[-1][2], st[-1][3]), (pos, dirs, idx)):
                #print(st, i)
                if st[-1][1] > hp:
                    st[-1][1] -= 1
                    hp = 0
                    break
                elif st[-1][1] < hp:
                    st.pop()
                    hp -= 1
                else:
                    st.pop()
                    hp = 0
                    break
            
            if hp > 0:
                st.append([pos, hp, dirs, idx])
            #print(st)
            
        
        st.sort(key=lambda x: x[3])
        res = []
        for i in st:
            res.append(i[1])
        
        return res