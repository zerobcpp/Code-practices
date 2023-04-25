def convertToBase7(n):
    if n < 0: return '-' + convertToBase7(-n)
    if n < 8: return str(n)
    return convertToBase7(n // 8) + str(n % 8)



if __name__ == '__main__':
    print(convertToBase7(119808))


