def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i].split(',')]
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

from collections import defaultdict


with open('d9.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
convert_list(inputs, True)

def part1():
    p1 = 0
    N = len(inputs)

    horizontal = defaultdict(set)
    vertical = defaultdict(set)
    nn = mm = 0

    for i in range(N):
        px, py = inputs[i]
        for j in range(i+1, N):
            qx, qy = inputs[j]
            
            length = abs(qx - px) + 1
            width = abs(qy - py) + 1
            area = length * width
            #print(px, py, qx, qy, area)
            p1 = max(p1, area)
        
        nn = max(nn, py)
        mm = max(mm, px)
        horizontal[py].add(px)
        vertical[px].add(py)
    
    print(p1)
    return p1

#try flooding it out
def part2():
    
    def gmm(x1, y1, x2, y2):
        return [min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)]
    
    N = len(inputs)
    p2 = 0
    seen = set()
    
    # get an shape of data that is responsible for the outside edge
    for i in range(N):
        x1, y1 = inputs[i]
        x2, y2 = inputs[(i+1)%N]
        
        mm = gmm(x1, y1, x2, y2)
        if x1 == x2:
            for j in range(mm[2], mm[3] + 1):
                seen.add((x1, j))
        else:
            for j in range(mm[0], mm[1] + 1):
                seen.add((j, y1))
    #print(seen)
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = inputs[i]
            x2, y2 = inputs[j]
            
            l = abs(x2 - x1) + 1
            w = abs(y2 - y1) + 1 
            a = l * w
            mm = gmm(x1, y1, x2, y2)
            good = True
            if a < p2:
                continue
            for sx, sy in seen:
                if mm[0] < sx < mm[1] and mm[2] < sy < mm[3]:
                    good = False
                    break
            
            if good:
                #print(x1, y1, x2, y2)
                if a > p2:
                    p2 = a
                    print(p2)
    
    print(p2)
    return p2
    

part2()
            
            





