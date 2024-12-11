with open('d10.txt', 'r+') as f:
    inputs = f.read()
dist4 = [0, -1, 0, 1, 0]

inputs = inputs.split('\n')
N = len(inputs)

for i in range(N):
    inputs[i] = [int(i) for i in inputs[i]]
M = len(inputs[0])
#print(inputs, N, M)

start = []
end = set()
for i in range(N):
    for j in range(M):
        if inputs[i][j] == 0:
            start.append([i, j, 0])
        elif inputs[i][j] == 9:
            end.add((i, j))

res = 0

def p1():
    def helper(i, j, cnt):
        st = [(i, j , cnt)]
        seen = set()
        seen.add((i, j))
        p1 = 0
        while st:
            x, y, step = st.pop()
            
            if step == 9:
                p1 += 1
                continue

            for i in range(4):
                dx, dy = x + dist4[i], y + dist4[i+1]
                if 0 <= dx < N and 0 <= dy < M:
                    if (dx, dy) not in seen and inputs[dx][dy] == step + 1:
                        seen.add((dx, dy))
                        st.append((dx, dy, step + 1))
        
        return p1
        
    p1 = 0
    for i, j, step in start:
        p1 += helper(i, j, 0)

    #print(p1)


            

def p2():
    from collections import defaultdict
    from collections import deque
    
    c = defaultdict(int)
    def helper(i, j, cnt):
        
        st = deque([(i, j , cnt)])
        path = set()
        
        while st:
            x, y, step = st.popleft()
            #print(x, y, end = '\t')
            if step == 9:
                c[(x, y)] += 1
                continue

            for i in range(4):
                dx, dy = x + dist4[i], y + dist4[i+1]
                if 0 <= dx < N and 0 <= dy < M:
                    if inputs[dx][dy] == step + 1:
                        st.append((dx, dy, step + 1))
            #print(st)
        
        return c
        
    p2 = 0
    for i, j, step in start:
        helper(i, j, 0)
    
    for i, v in c.items():
        p2 += v
    print(c)
    print(p2)

p2()


            

