cast = [int(i) for i in input().split(" ")]
x = cast[0]
y = cast[1]
z = cast[2]

if x - y == 0 and z == 0:
    print("0")
elif x > y + z:
    print("+")
elif y > x + z:
    print("-")
else:
    print("?")
