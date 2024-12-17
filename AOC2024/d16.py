def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr

def d8(x, y):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                cords.append((x+i, y+j))
    return cords

d4 = [0, -1, 0, 1, 0]
dr = {
    0: [0, -1], #<
    1: [-1, 0], #^
    2: [0, 1],  #>
    3: [1, 0],  #v
}



with open('d16.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

convert_list(inputs)
N = len(inputs)
M = len(inputs)
g = inputs
start = None
end = None
for i in range(N):
    for j in range(M):
        if g[i][j] == 'S':
            start = (i, j)
            g[i][j] = '.'
        elif g[i][j] == 'E':
            end = (i, j)
            g[i][j] = '.'
    
    if start and end:
        break



def get_score(turn, step):
    return turn * 1000 + step

import heapq
from collections import defaultdict

cost = defaultdict(lambda: float('inf'))
st = [(0, 0, 2, start[0], start[1])]
cost[start[0], start[1], 2] = 0

allpaths = defaultdict(set)
cand = set()
best = 0
while st:
    turn, step, dirs, x, y = heapq.heappop(st)
    
    if (x, y, ) == end:
        print(get_score(turn, step))
        cand.add((x, y, dirs))
        break


    for k in range(4):
        dx, dy = x + d4[k] , y + d4[k+1]
        
        if g[dx][dy] not in '#':
            if cost[x, y, dirs] + 1001 < cost[dx, dy, k] and k != dirs:
                cost[dx, dy, k] = cost[x, y, dirs] + 1001
                heapq.heappush(st, (turn + 1, step + 1, k, dx, dy))
                allpaths[dx, dy, k].add((x, y, dirs))
                
            elif cost[x, y, dirs] + 1001 == cost[dx, dy, k] and k != dirs:
                allpaths[dx, dy, k].add((x, y, dirs))
            
            
            if cost[x, y, dirs] + 1 < cost[dx, dy, k] and k == dirs:
                cost[dx, dy, k] = cost[x, y, dirs] + 1
                heapq.heappush(st, (turn, step + 1, k, dx, dy))
                allpaths[dx, dy, k].add((x, y, dirs))
            elif cost[x, y, dirs] + 1 == cost[dx, dy, k] and k == dirs:
                allpaths[dx, dy, k].add((x, y, dirs))



print(cand)
common = set(cand)

for x, y, k in cand:
    st = [(x, y, k)]
    seen = set()
    while st:
        ix, iy, ik = st.pop()
        
        for dx, dy, drs in allpaths[ix, iy, ik]:
            if (dx, dy, drs) not in seen:
                seen.add((dx, dy, drs))
                st.append((dx, dy, drs))

        common.update(seen)
        
pts = set()
for dx, dy, dr in common:
    pts.add((dx, dy))

print(len(pts))
for i in range(N):
    for j in range(M):
        if (i, j) in pts:
            print('O', end = ' ')
        else:
            print(g[i][j], end =' ')
    print()
#print(len(common))
#print(common)
    
    #print(seen)
    #print(st)


# if (x, y) == end:
#     path = get_score(turn, step)
#     if (x, y) not in score:
#         score[(x, y)] = path
#         allpaths[(x,y)] = seen
#         best = len(seen)
#     else:
#         if score[(x, y)] == path:
#             for cx, cy in seen:
#                 if (cx, cy) not in allpaths[(x,y)]:
#                     allpaths[(x,y)].add((cx, cy))
#             best = max(best, len(allpaths[(x,y)]))
#         elif path > score[(x, y)]:
#             score[(x, y)] = path
#             allpaths[(x,y)] = seen
#             best = len(seen)
        