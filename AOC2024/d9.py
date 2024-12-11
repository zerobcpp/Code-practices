with open('d9.txt', 'r+') as f:
    inputs = f.read()



inputs = list(inputs)


def p1():
    blocks = []
    N = len(inputs)
    print(N)

    import heapq
    id = 0
    p = False

    for i in range(N):
        if not p:
            for j in range(int(inputs[i])):
                blocks.append(str(id))
            
            id += 1
        else:
            for j in range(int(inputs[i])):
                blocks.extend('.')
        p = not p
        

    r = len(blocks) - 1
    l = 0
    while l < r:

        while l < r and blocks[l] != '.':
            l += 1
        while r > l and blocks[r] == '.':
            r -= 1
        blocks[l], blocks[r] = blocks[r], blocks[l]

    i = 0
    p1 = 0
    print(len(blocks))
    while i < len(blocks):
        if blocks[i] == '.':
            break
        p1 += int(blocks[i]) * i
        i += 1

    print(p1)



#6242504872659
#6242766528339
#6242766523059

def p2():
    blocks = []
    N = len(inputs)
    print(N)

    import heapq
    id = 0
    p = False
    
    bmap = {}
    cmap = {}

    for i in range(N):
        if not p:
            for j in range(int(inputs[i])):
                blocks.append(str(id))
            cmap[str(id)] = int(inputs[i])
            id += 1
        else:
            for j in range(int(inputs[i])):
                blocks.extend('.')
            bmap[str(id-1)] = int(inputs[i])
        p = not p
    
    
    last = id
    cur = 0
    l = 0
    #print(bmap, cmap)
    #print(blocks)
    N = len(blocks)
    l = 0
    while last > 0:
        lcnt = cmap.get(str(last), 0)
        if lcnt == 0:
            last -= 1
            continue

        loop = False
        fcnt = 0
        for i in range(N):
            if blocks[i] == str(last):
                break
            if blocks[i] == '.':
                fcnt += 1
            else:
                l = i + 1
                fcnt = 0
            
            
            if fcnt >= lcnt:
                cur += 1
                loop = True
                #print(fcnt, lcnt, end = ' ')
                for j in range(N-1, -1, -1):
                    if blocks[j] == str(last):
                        blocks[j] = '.'
                    if blocks[j] != '.' and int(blocks[j]) < last:
                        break

                for j in range(l, l+lcnt):
                    blocks[j] = str(last)
            
            
            if loop:
                #print(blocks)
                break
                
                
        last -= 1 
    
    cur = 0
    p2 = 0
    for i in range(N):
        if blocks[i] != '.':
            p2 += int(blocks[i]) * cur
        cur += 1
    
    print(p2)
    print(blocks)







p2()