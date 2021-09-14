n = input()
num = '0'
sum = 1

for i in range(len(n)-1):
    if n[i] == n[i+1]:
        sum +=1
    else:
        num = n[i]
        sum = 1
    if sum>= 7:
        break

if sum >= 7:
    print("YES")
else:
    print("NO")