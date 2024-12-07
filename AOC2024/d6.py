with open('d6.txt', 'r+') as f:
    inputs = f.read()

inputs = inputs.split('\n')
for i in range(len(inputs)):
    inputs[i] = list(inputs[i])
#print(inputs)
dirs = {
    0: [-1, 0], #^
    1: [0, 1],  #>
    2: [1, 0],  #v
    3: [0, -1], #<
}
N = len(inputs)
M = len(inputs[0])
start = []
for i in range(N):
    found = False
    for j in range(M):
        if inputs[i][j] not in '.#':
            start.append((i, j, 0))
            found = True
            break
    if found:
        break

seen = set()
seen.add((i, j))
X, Y = (i, j)
while start:
    x, y, d = start.pop()
    mode = dirs[d]
    dx, dy = x + mode[0], y + mode[1]
    if dx < 0 or dx >= N or dy < 0 or dy >= M:
        break
    if inputs[dx][dy] == '#':
        d = (d + 1) % 4
        mode = dirs[d]
        dx, dy = x + mode[0], y + mode[1]
        start.append((dx, dy, d))
    else:
        start.append((dx, dy, d))
    
    
    seen.add((dx, dy))

print(len(seen)) #p1

p2 = 0
for i in range(N):
    for j in range(M):
        if inputs[i][j] == '.':
            inputs[i][j] = '#'
            start = [(X, Y, 0)]
            seen = set()
            seen.add((X, Y))
            
            while start:
                x, y, d = start.pop()

                
                mode = dirs[d]
                dx, dy = x + mode[0], y + mode[1]
                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                    break
                while inputs[dx][dy] == '#':
                    d = (d + 1) % 4
                    mode = dirs[d]
                    dx, dy = x + mode[0], y + mode[1]
                    start.append((dx, dy, d))
                else:
                    start.append((dx, dy, d))
                
                if (dx, dy, d) in seen:
                    p2 += 1
                    print(i, j, d)
                    break
                #print(dx, dy, d)
                seen.add((dx, dy, d))
                
            
            inputs[i][j] = '.'

print(p2)


#1893 too low
#1995 right - change to (while)





