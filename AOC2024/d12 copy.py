def convert_list(arr, toInt=False):
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


def p1():
    c = {}
    seen = set()
    from collections import deque
    for i in range(N):
        for j in range(M):
            if (i, j) not in seen:
                start = deque([(i, j)])
                same = inputs[i][j]
                sides = set()
                seen.add((i, j))
                sides.add((i, j))
                tot = 0
                while start:
                    x, y = start.pop()

                    tot += 1
                    for k in range(4):
                        dx, dy = x + dist4[k], y + dist4[k+1]
                        if 0 <= dx < N and 0 <= dy < M:
                            if inputs[dx][dy] == same and (dx, dy) not in seen:
                                start.append((dx, dy))
                                seen.add((dx, dy))
                                sides.add((dx, dy))

                side = 0
                for x, y in sides:
                    for k in range(4):
                        dx, dy = x + dist4[k], y + dist4[k+1]
                        if (dx, dy) not in sides:
                            side += 1

                c[same] = c.get(same, [])
                c[same].append([tot, side])

    #print(c)
    p1 = 0
    for i, v in c.items():
        for a, p in v:
            p1 += a * p

    print(p1)


def p2():
    c = {}
    seen = set()
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

                perim = set()
                side = 0
                for x, y in sides:
                    for k in range(4):
                        dx, dy = x + dist4[k], y + dist4[k+1]
                        if (dx, dy) not in sides:
                            perim.add((x, y, dx, dy))

                # print(same, side)

                for x, y, x1, y1 in perim:
                    keep = True
                    for dx, dy in [(1, 0), (0, 1)]:
                        if (x+dx, y+dy, x1+dx, y1+dy) in perim:
                            keep = False
                            break
                    if keep:
                        side += 1

                c[same] = c.get(same, [])
                c[same].append([tot, side])

    # print(c)
    p2 = 0
    for i, v in c.items():
        for j in v:
            p2 += j[0] * j[1]

    print(p2)


p1()
p2()
