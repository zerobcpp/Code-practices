def convertToBase7(n):
    if n < 0: return '-' + convertToBase7(-n)
    if n < 16: return str(n)
    return convertToBase7(n // 16) + str(n % 16)



if __name__ == '__main__':
    print(convertToBase7(119808))


