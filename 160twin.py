n = int(input())
coin = [int(i) for i in input().split(" ")]

coin.sort()
coinsum = sum(coin)
sum = 0
take = 1

for i in coin:
    if sum + i > coinsum/2:
        break
    else:
        take += 1
        sum = sum + i

print(take)