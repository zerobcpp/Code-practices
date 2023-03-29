# 371



def sumwithoutadd(a: int, b: int) -> int:
    if not a:
        return b
    if not b:
        return a

    # res = 0
    while b != 0:
        carry = ((a & b) << 1) & 0xFFFFFFFF
        a = (a ^ b) & 0xFFFFFFFF
        b = carry
    return a if a < 0x7fffffff else ~(a^0xFFFFFFFF)

a = 1
b = -1

print(bin(a & b))
# print(bin(a^b))
print(hex(a))
print(hex(b))
# print(bin(a+b))

print(sumwithoutadd(a,b))


