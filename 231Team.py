n = int(input())
problem = []
for i in range(n):
    anw = input()
    a = anw.split(" ")
    set = [a[0], a[1], a[2]]
    problem.append(set)

sure = 0
for i in range(n):
    s = 0
    for j in range(len(problem[i])):
        if problem[i][j] == '1':
            s += 1
            if s >= 2:
                sure += 1
                break

print(sure)