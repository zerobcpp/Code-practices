with open('d8.txt', 'r+') as f:
    inputs = f.read()

inputs = inputs.split('\n')

N = len(inputs)
M = len(inputs[0])

for i in range(N):
    inputs[i] = list(inputs[i])

from collections import defaultdict
c = defaultdict(list)
for i in range(N):
    for j in range(M):
        if inputs[i][j] != '.':
            c[inputs[i][j]].append((i, j))

def part1():
    st = set()
    for k, v in c.items():
        P = len(v)
        for i in range(P):
            x, y = v[i]
            for j in range(P):
                if i != j:
                    xx, yy = v[j]
                    dx, dy = (xx - x), (yy - y)
                    
                    
                    cx, cy = x - dx, y - dy
                    if 0 <= cx < N and 0 <= cy < M:
                        st.add((cx, cy))
                     
                    cx, cy = xx + dx, yy + dy
                    if 0 <= cx < N and 0 <= cy < M:
                        st.add((cx, cy))
    print(len(st))




def part2():
    st = set()
    for k, v in c.items():
        P = len(v)
        for i in range(P):
            x, y = v[i]
            for j in range(P):
                if i != j:
                    xx, yy = v[j]
                    dx, dy = (xx - x), (yy - y)
                    
                    cx, cy = x, y
                    # negative side
                    while 0 <= cx < N and 0 <= cy < M:
                        st.add((cx, cy))
                        cx -= dx
                        cy -= dy
                    
                    cx, cy = xx, yy
                    while 0 <= cx < N and 0 <= cy < M:
                        st.add((cx, cy))
                        cx += dx
                        cy += dy
    
    print(len(st))

part1()
part2()
