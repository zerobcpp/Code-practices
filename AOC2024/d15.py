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

mv = {
'<':[0, -1],
'^':[-1, 0],
'>':[0, 1], 
'v':[1, 0], 
}




with open('d15.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

N = len(inputs)
mark = 0
for i in range(N):
    
    if not inputs[i]:
        mark = i
        break


graph = inputs[:mark]






moves = []
for i in range(mark, len(inputs)):
    moves.extend(inputs[i])

convert_list(graph)
N = len(graph)
M = len(graph[0])

def p1():
    N = len(graph)
    M = len(graph[0])
    for i in range(N):
        found = False
        for j in range(M):
            if graph[i][j] == '@':
                x, y = (i, j)
                graph[i][j] = '.'
                found = True
                break
        if found:
            break
    for action in moves:
        dx, dy = mv[action]
        xx, yy = x + dx, y + dy
        print(x, y, action)
        
        if graph[xx][yy] == '#':
            continue
        elif graph[xx][yy] == '.':
            x, y = xx, yy
            
        elif graph[xx][yy] == 'O':
            while graph[xx][yy] == 'O':
                xx += dx
                yy += dy
            
            if graph[xx][yy] == '#':
                continue
            elif graph[xx][yy] == '.':
                while (xx, yy) != (x, y):
                    graph[xx][yy] = graph[xx-dx][yy-dy]
                    xx -= dx
                    yy -= dy
                
                x += dx
                y += dy

                    
                             
        
    p1 = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'O':
                p1 += 100 * i + j
                
    
    print(p1)



new_graph = []
for i in range(N):
    temp = []
    for j in range(M):
        if graph[i][j] == '.':
            temp.extend('..')
        elif graph[i][j] == 'O':
            temp.extend('[]')
        elif graph[i][j] == '#':
            temp.extend('##')        
        else:
            temp.extend('@.')
    new_graph.append(list(temp))

N = len(new_graph)
M = len(new_graph[0])


for i in range(N):
    found = False
    for j in range(M):
        if new_graph[i][j] == '@':
            x, y = (i, j)
            new_graph[i][j] = '.'
            found = True
            break
    if found:
        break
print(x, y)
for i in new_graph:
    print(i)
for action in moves:
    dx, dy = mv[action]
    xx, yy = x + dx, y + dy
    
    
    if new_graph[xx][yy] == '#':
        continue
    elif new_graph[xx][yy] == '.':
        x, y = xx, yy
        
    elif new_graph[xx][yy] in '[]':
        st = [(x, y)]
        seen = set()
        
        PUSH = True
        while st:
            tx, ty = st.pop()
            if (tx, ty) in seen:
                continue
            seen.add((tx, ty))
            nx, ny = tx + dx, ty + dy
            if new_graph[nx][ny] == '#':
                PUSH = False
                break
            if new_graph[nx][ny] == '[':
                st.append([nx, ny])
                
                st.append([nx,ny+1]) #]
            if new_graph[nx][ny] == ']':
                st.append([nx, ny])
                
                st.append([nx,ny-1]) #[
        if not PUSH:
            continue
        
        while len(seen) > 0:
            for tx, ty in sorted(seen):
                nx, ny = tx + dx, ty + dy
                if (nx, ny) not in seen:
                    
                    new_graph[nx][ny] = new_graph[tx][ty]
                    new_graph[tx][ty] = '.'
                    seen.remove((tx, ty))
        x += dx
        y += dy
            
        # for i in new_graph:
        #     print(i)
    

            
p2 = 0
for i in range(N):
    for j in range(M):
        if new_graph[i][j] == '[':
            p2 += 100 * i + j

print(p2)