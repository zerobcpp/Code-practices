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

# part 2
size = max(nn, mm)
print(size, nn, mm)
print("p2 start")


# seems like memory problem with this, so do we really need to form all the graph?, min, max and check the range?
#grid = [['.']  * (size+1) for _ in range(size+1)]

#print(grid)
gh = vertical.copy()
gv = horizontal.copy()
ghm = defaultdict(lambda: [10 ** 9,-1])
gvm = defaultdict(lambda: [10 ** 9, -1])

for i, v in horizontal.items():
    for k in range(min(v), max(v)+1):  # horizontal forming X
        #grid[i][k] = 'X'    
        gh[k].add(i)


for i, v in vertical.items():
    for k in range(min(v), max(v)+1):
        gv[k].add(i)
    
#print('Slow?')
for i, v in gh.items():
    ghm[i][0] = min(v)
    ghm[i][1] = max(v)

for i, v in gv.items():
    gvm[i][0] = min(v)
    gvm[i][1] = max(v)



        

#print(ghm, gvm, sep = '\n')
    
# C = '   '
# for i in range(mm+2):
#    print(C, i, end ='')
# print()    
# for i, v in enumerate(grid):
#    print(i, v)

#(2, 3)                 #(3, 9)
                        #(5, 9)
# print(gh)

#print(gvm, ghm, sep = '\n')
p2 = 0
for i in range(N):
    px, py = inputs[i]
    for j in range(i+1, N):
        qx, qy = inputs[j]
        
        #print(CORNERS)
        mnx = min(px, qx)
        mny = min(py, qy)
        mxx = max(px, qx)
        mxy = max(py, qy)
        #make sure the area is actually flooded or within the range
        print(px, py, qx, qy)
        
        good = True
        
        for x in range(mnx, mxx+1):
            if x not in ghm or (x in ghm and mny < ghm[x][0] or mxy > ghm[x][1]):
                good = False
                break
    
        for y in range(mny, mxy+1):
            if y not in gvm or (y in gvm and mnx < gvm[y][0] or mxx > gvm[y][1]):
                good = False
                break

        if good:
            length = abs(px - qx) + 1
            width = abs(qy - py) + 1
            area = length * width
            #print(px, py, qx, qy)
            print(area)
            if area > p2:
                print(area)
                p2 = area
    
    
print('end = ', p2)

        


# (qx, py)
# (px, qy)
# #5 9 3 2 # .

# need to get (3, 9) and (5, 2)
#4586842110 too high
#4482663810 too high
#4733727792
#2648107644 high
#138819244 close?
# wtf is going on?