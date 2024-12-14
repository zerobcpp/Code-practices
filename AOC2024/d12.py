def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr

dist4 = [0, -1, 0, 1, 0]



with open('d12.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
convert_list(inputs)

N = len(inputs)
M = len(inputs[0])

c = {}
seen = set()
def p1():
    for i in range(N):
        for j in range(M):
            if (i, j) not in seen:
                start = [(i, j)]
                seen.add((i, j))
                same = inputs[i][j]
                sides =  0
                tot = 0
                while start:
                    x, y = start.pop()
                    tot += 1
                    side = 4
                    for k in range(4):
                        dx, dy = x + dist4[k], y + dist4[k+1]
                        if 0 <= dx < N and 0 <= dy < M:
                            if inputs[dx][dy] == same:
                                side -= 1   
                            if (dx, dy) not in seen and inputs[dx][dy] == same:
                                start.append((dx, dy))
                                seen.add((dx, dy))
                                
                                
                    sides += side


                c[same] = c.get(same, [])
                c[same].append([tot, sides])

                
    print(c)
    p1 = 0
    for i, v in c.items():
        for a, p in v:
            p1 += a * p

    print(p1)



def p2():
    for i in range(N):
        for j in range(M):
            if (i, j) not in seen:
                start = [(i, j)]
                seen.add((i, j))
                same = inputs[i][j]
                sides = set()
                sides.add((i, j))
                tot = 0
                while start:
                    x, y = start.pop()
                    tot += 1
                    
                    for k in range(4):
                        dx, dy = x + dist4[k], y + dist4[k+1]
                        if 0 <= dx < N and 0 <= dy < M:
                            if (dx, dy) not in seen and inputs[dx][dy] == same:
                                start.append((dx, dy))
                                seen.add((dx, dy))
                                sides.add((dx, dy))
                
                #print(same, sides)
                side = 0            
                
                for x, y in sorted(sides):
                    for nx,ny,x1,y1,x2,y2 in [(x-1,y, x,y-1,x-1,y-1),
                                              (x,y-1, x-1,y,x-1,y-1),
                                              
                                              (x,y+1, x-1,y,x-1,y+1),
                                              (x+1,y, x,y-1,x+1,y-1),
                                              ]:
                        if (nx, ny) not in sides and ((x1, y1) not in sides or (x2, y2) in sides):
                            side += 1
                    
                    print(f'{x=}, {y=}, {side=}')
                    
                c[same] = c.get(same, [])
                c[same].append([tot, side])
            

                
    
    p2 = 0
    for i, v in c.items():
        for j in v:
            p2 += j[0] * j[1]

    print(p2)
p2()
                    