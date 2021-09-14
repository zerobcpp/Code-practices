n = input()
nsplit = n.split(' ')
n = int(nsplit[0])
k = int(nsplit[1])
a = input()
aret = a.split(' ')
alist = [int(i) for i in aret]

iteration = 0
upper = alist[k-1]
for i in range(n):
    if alist[i] != 0 and alist[i] >= upper:
        iteration += 1

print(iteration)