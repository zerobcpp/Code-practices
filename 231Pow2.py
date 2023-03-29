def isPower2(n):
    print(n, f'{n:08b}')
    print(n-1, f'{n-1:08b}')
    print(n-(n-1), f'{n-(n-1):08b}')

def hammingWeight( n):
    ans = 0
    while n:
        print(f'{n:02b}')
        print(f'{n-1:02b}')
        print ("----")
        n &= (n-1)
        ans += 1

    return ans

#isPower2(32)
hammingWeight(1021210)